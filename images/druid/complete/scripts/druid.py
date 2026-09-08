#!/usr/bin/env python3
"""Reproducible command-line runner for the DRUID complete-analysis tutorial."""
import argparse
import csv
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone

HOME = Path(os.environ.get('DRUID_HOME', '/opt/DRUID'))
HERE = Path(__file__).resolve().parent


def run(args, cwd=None, output=None, env=None):
    args = [str(a) for a in args]
    print('+ ' + ' '.join(args), flush=True)
    if output:
        with Path(output).open('w') as handle:
            subprocess.run(args, cwd=cwd, env=env, stdout=handle, check=True)
    else:
        subprocess.run(args, cwd=cwd, env=env, check=True)


def digest(path, kind='sha256'):
    h = hashlib.new(kind)
    with Path(path).open('rb') as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def download(url, path, md5=None):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if md5 and digest(path, 'md5') != md5:
            raise ValueError(f'Checksum mismatch for existing file: {path}; move it aside before retrying')
        print(f'Using {path}', flush=True)
        return
    partial = path.with_name(path.name + '.partial')
    run(['curl', '-fL', '--retry', '5', '--retry-delay', '3', '-C', '-', url, '-o', partial])
    if md5 and digest(partial, 'md5') != md5:
        raise ValueError(f'Checksum mismatch: {partial}; remove this partial download before retrying')
    partial.rename(path)


def samples(args):
    with args.manifest.open() as handle:
        rows = list(csv.DictReader(handle, delimiter='\t'))
    if len(rows) < 4:
        raise ValueError('At least four time points are required for leave-one-out fitting')
    for r in rows:
        if not re.fullmatch(r'[A-Za-z0-9_.-]+', r['sample']):
            raise ValueError(f'Invalid sample identifier: {r["sample"]}')
        if float(r['time_hours']) <= 0:
            raise ValueError('Approach-to-equilibrium time points must be positive')
    if len({r['sample'] for r in rows}) != len(rows) or len({float(r['time_hours']) for r in rows}) != len(rows):
        raise ValueError('Samples and time points must be unique')
    return sorted(rows, key=lambda r: float(r['time_hours']))


def memory_check():
    # Check both Linux physical memory and container cgroup limits.
    limits = []
    meminfo = Path('/proc/meminfo')
    if meminfo.exists():
        limits.append(int(re.search(r'MemTotal:\s+(\d+)', meminfo.read_text())[1]) * 1024)
    for p in ('/sys/fs/cgroup/memory.max', '/sys/fs/cgroup/memory/memory.limit_in_bytes'):
        if Path(p).exists():
            value = Path(p).read_text().strip()
            if value.isdigit():
                limits.append(int(value))
    if limits and min(limits) < 30 * 1024**3:
        raise RuntimeError('The combined human/fly/yeast workflow requires at least 32 GB assigned to Docker (40 GB recommended). The current memory limit is too low.')


def fetch_fastq(args):
    for r in samples(args):
        download(r['url'], args.work / 'RawSequencingData' / args.dataset / (r['sample'] + '.fastq.gz'), r['md5'])


def unpack_genepred(annotation, target, table):
    import gzip
    with gzip.open(annotation, 'rt') as src, open(target, 'w') as dst:
        for line in src:
            fields = line.rstrip('\n').split('\t')[1:]  # discard UCSC bin
            # sgdGene appends proteinID, not genePredExt's score/name2 fields.
            if table == 'sgdGene':
                fields = fields[:10]
            dst.write('\t'.join(fields) + '\n')


def label_reference(fasta, gtf, suffix, filtered, outfa, outgtf):
    # Exactly the tutorial's canonical-chromosome filter; yeast retains all contigs.
    keep = False
    with open(fasta) as src, open(outfa, 'w') as dst:
        for line in src:
            if line.startswith('>'):
                name = line[1:].strip()
                keep = not filtered or bool(re.fullmatch(r'chr[0-9A-Z]{1,2}', name))
                if keep:
                    dst.write('>' + name + suffix + '\n')
            elif keep:
                dst.write(line)
    with open(gtf) as src, open(outgtf, 'w') as dst:
        for line in src:
            if line.startswith('#'):
                continue
            fields = line.rstrip('\n').split('\t')
            if len(fields) != 9:
                continue
            if filtered and not re.fullmatch(r'chr[0-9A-Z]{1,2}', fields[0]):
                continue
            fields[0] += suffix
            fields[8] = re.sub(r'((?:gene_id|transcript_id|exon_id|gene_name) ")([^"]+)(")',
                               lambda m: m[1] + m[2] + suffix + m[3], fields[8])
            dst.write('\t'.join(fields) + '\n')


def prepare_reference(args):
    if not args.small_genome:
        memory_check()
    base = args.work / 'ExternalData'
    ref = base / 'Genomes' / 'hg38dm6sacCer3'
    index = base / 'IndexedGenomes' / 'hg38dm6sacCer3_50'
    ref.mkdir(parents=True, exist_ok=True)
    index.mkdir(parents=True, exist_ok=True)
    fa, gtf = ref / 'hg38dm6sacCer3.fa', ref / 'hg38dm6sacCer3.gtf'
    if bool(args.fasta) != bool(args.gtf):
        raise ValueError('Supply both --fasta and --gtf (already labeled and filtered)')
    if args.fasta:
        shutil.copyfile(args.fasta, fa)
        shutil.copyfile(args.gtf, gtf)
    else:
        fastas, gtfs = [], []
        for genome, table, suffix, filtered in [('hg38', 'refGene', 'h', True), ('dm6', 'refGene', 'f', True), ('sacCer3', 'sgdGene', 'y', False)]:
            folder = base / 'Genomes' / genome
            folder.mkdir(parents=True, exist_ok=True)
            bit = folder / f'{genome}.2bit'
            annotation = folder / f'{table}.txt.gz'
            download(f'https://hgdownload.soe.ucsc.edu/goldenPath/{genome}/bigZips/{genome}.2bit', bit)
            download(f'https://hgdownload.soe.ucsc.edu/goldenPath/{genome}/database/{table}.txt.gz', annotation)
            run(['twoBitToFa', bit, folder / 'genome.fa'])
            # UCSC table dumps contain a leading bin field; file input avoids remote MySQL.
            unpack_genepred(annotation, folder / 'genes.gp', table)
            run(['genePredToGtf', '-utr', 'file', folder / 'genes.gp', folder / 'genes.gtf'])
            label_reference(folder / 'genome.fa', folder / 'genes.gtf', suffix, filtered,
                            folder / 'labeled.fa', folder / 'labeled.gtf')
            fastas.append(folder / 'labeled.fa')
            gtfs.append(folder / 'labeled.gtf')
        for sources, target in [(fastas, fa), (gtfs, gtf)]:
            with target.open('wb') as out:
                for source in sources:
                    with source.open('rb') as src:
                        shutil.copyfileobj(src, out)
    run(['Rscript', HOME / 'process_GTF.R', gtf])
    for suffix in ('exons.gtf', 'exons.no.gtf', 'introns.gtf'):
        if not (ref / f'hg38dm6sacCer3.{suffix}').stat().st_size:
            raise ValueError(f'Empty annotation: {suffix}')
    run(['samtools', 'faidx', fa])
    with open(str(fa) + '.fai') as handle:
        sizes = sorted((line.split('\t')[:2] for line in handle), key=lambda r: r[0])
    (ref / 'sizes.genome').write_text(''.join('\t'.join(r) + '\n' for r in sizes))
    command = ['STAR', '--runThreadN', args.threads, '--runMode', 'genomeGenerate', '--genomeDir', index,
               '--genomeFastaFiles', fa, '--sjdbGTFfile', gtf, '--genomeSAsparseD', '2', '--sjdbOverhang', '50',
               '--limitGenomeGenerateRAM', '31000000000']
    if args.small_genome:
        command += ['--genomeSAindexNbases', '6', '--genomeChrBinNbits', '12']
    run(command, cwd=index)
    provenance = {'created_utc': datetime.now(timezone.utc).isoformat(), 'small_genome': args.small_genome,
                  'fasta_sha256': digest(fa), 'gtf_sha256': digest(gtf)}
    (ref / 'provenance.json').write_text(json.dumps(provenance, indent=2) + '\n')


def analyze(args):
    rows = samples(args)
    ref = args.work / 'ExternalData/Genomes/hg38dm6sacCer3'
    index = args.work / 'ExternalData/IndexedGenomes/hg38dm6sacCer3_50'
    provenance = json.loads((ref / 'provenance.json').read_text())
    if not provenance['small_genome']:
        memory_check()
    analysis = args.work / 'Analysis' / args.dataset
    if analysis.exists():
        raise RuntimeError(f'Analysis directory already exists: {analysis}. Use `druid fit` to repeat fitting, or move the analysis aside before rerunning.')
    raw = args.work / 'RawSequencingData' / args.dataset
    fastqs = [raw / (r['sample'] + '.fastq.gz') for r in rows]
    for path in fastqs:
        if not path.is_file():
            raise FileNotFoundError(path)
    for name in ('FastQC', 'TrimmedReads', 'STAR', 'BAM', 'Logs', 'htseq_exons_introns'):
        (analysis / name).mkdir(parents=True, exist_ok=True)
    (analysis / 'data.files.txt').write_text(''.join(str(p) + '\n' for p in fastqs))
    # Limit simultaneous QC memory; other tools use the full thread budget.
    run(['fastqc', '--outdir', analysis / 'FastQC', '--threads', min(args.threads, 4), *fastqs])
    logs = []
    for r, fq in zip(rows, fastqs):
        sample = r['sample']
        trimmed = analysis / 'TrimmedReads' / fq.name
        run(['java', '-jar', '/opt/trimmomatic.jar', 'SE', '-threads', args.threads, '-phred33', fq, trimmed,
             'ILLUMINACLIP:/opt/trimmomatic/TruSeq3-SE.fa:2:30:10', 'LEADING:3', 'TRAILING:3', 'SLIDINGWINDOW:4:15', 'MINLEN:36'])
        star = analysis / 'STAR' / sample
        star.mkdir()
        run(['STAR', '--runThreadN', args.threads, '--genomeDir', index, '--readFilesIn', trimmed,
             '--readFilesCommand', 'zcat', '--outFilterMultimapNmax', '10', '--outFilterMismatchNoverLmax', '0.05',
             '--outFilterScoreMinOverLread', '0.75', '--outFilterMatchNminOverLread', '0.85', '--alignIntronMax', '1',
             '--outFilterIntronMotifs', 'RemoveNoncanonical', '--outSAMtype', 'BAM', 'SortedByCoordinate',
             '--quantMode', 'GeneCounts', '--limitBAMsortRAM', '4000000000', '--genomeLoad', 'NoSharedMemory'], cwd=star)
        bam = analysis / 'BAM' / (sample + '.bam')
        shutil.move(star / 'Aligned.sortedByCoord.out.bam', bam)
        run(['samtools', 'quickcheck', bam])
        run(['samtools', 'index', '-@', args.threads, bam])
        metrics = dict(line.strip().split('|', 1) for line in (star / 'Log.final.out').read_text().splitlines() if '|' in line)
        metrics = {k.strip(): v.strip() for k, v in metrics.items()}
        logs.append([sample] + [metrics[k] for k in ['Number of input reads', 'Uniquely mapped reads number', 'Number of reads mapped to multiple loci', 'Number of reads mapped to too many loci']])
        for feature, mode in [('exon', 'intersection-strict'), ('intron', 'union')]:
            annotation = ref / ('hg38dm6sacCer3.' + ('exons' if feature == 'exon' else 'introns') + '.gtf')
            run(['htseq-count', '--format=bam', '--order=pos', '--stranded=reverse', '--minaqual=10', '--type=exon',
                 '--idattr=gene_id', '--mode=' + mode, '--quiet', bam, annotation],
                output=analysis / 'htseq_exons_introns' / f'{sample}_{feature}.tsv')
    (analysis / 'Logs/Logs.tsv').write_text(''.join(' '.join(row) + '\n' for row in logs))
    run(['perl', HOME / 'Scripts/htseqGeneCountsMerge.pl'], cwd=analysis / 'htseq_exons_introns')
    env = os.environ.copy()
    env.update(GTF_NO_EXON=str(ref / 'hg38dm6sacCer3.exons.no.gtf'), GTF_INTRON=str(ref / 'hg38dm6sacCer3.introns.gtf'),
               GENOME_SIZES=str(ref / 'sizes.genome'), BAM_PATH=str(analysis / 'BAM'))
    run(['bash', HOME / 'preDRUID.sh'], cwd=analysis, env=env)
    shutil.copyfile(args.manifest, analysis / 'samples.tsv')
    shutil.copyfile('/opt/debian-packages.tsv', analysis / 'software-versions.tsv')
    shutil.copyfile(ref / 'provenance.json', analysis / 'reference-provenance.json')
    (analysis / 'workflow-provenance.json').write_text(json.dumps({
        'upstream_commit': (HOME / 'UPSTREAM_COMMIT').read_text().strip(),
        'script_sha256': {p.name: digest(p) for p in [HERE / 'druid.py', HERE / 'fit.R',
                            HOME / 'DRUID.R', HOME / 'coverage.py', HOME / 'preDRUID.sh', HOME / 'process_GTF.R']},
    }, indent=2) + '\n')
    fit(args)


def fit(args):
    analysis = args.work / 'Analysis' / args.dataset
    run(['Rscript', HERE / 'fit.R', analysis, args.manifest])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=['download', 'reference', 'analyze', 'fit', 'all', 'smoke-test'])
    parser.add_argument('--work', type=Path, default=Path.cwd(), help='Mounted working directory (default: current directory)')
    parser.add_argument('--manifest', type=Path, default=Path('/opt/config/HEK293_R1.tsv'))
    parser.add_argument('--dataset', default='HEK293_R1')
    parser.add_argument('--threads', type=int, default=int(os.environ.get('THREADS', '8')))
    parser.add_argument('--fasta', type=Path, help='Already species-labeled FASTA, with --gtf')
    parser.add_argument('--gtf', type=Path, help='Already species-labeled GTF, with --fasta')
    parser.add_argument('--small-genome', action='store_true', help='Small synthetic reference only; never use for the full human genome')
    args = parser.parse_args()
    args.work = args.work.resolve()
    args.manifest = args.manifest.resolve()
    if args.fasta: args.fasta = args.fasta.resolve()
    if args.gtf: args.gtf = args.gtf.resolve()
    if args.threads < 1 or not re.fullmatch(r'[A-Za-z0-9_.-]+', args.dataset) or args.dataset in ('.', '..'):
        parser.error('Threads must be positive and dataset must be a simple directory name')
    args.work.mkdir(parents=True, exist_ok=True)
    Path(os.environ.get('TMPDIR', str(args.work / 'tmp'))).mkdir(parents=True, exist_ok=True)
    if args.command == 'all':
        memory_check()
        fetch_fastq(args)
        prepare_reference(args)
        analyze(args)
    elif args.command == 'smoke-test':
        run(['bash', '/opt/tests/smoke-test.sh', args.work])
    else:
        {'download': fetch_fastq, 'reference': prepare_reference, 'analyze': analyze, 'fit': fit}[args.command](args)


if __name__ == '__main__':
    try:
        main()
    except (ValueError, RuntimeError, OSError, subprocess.CalledProcessError) as error:
        sys.exit(f'ERROR: {error}')
