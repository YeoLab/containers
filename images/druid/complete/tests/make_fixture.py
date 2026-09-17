#!/usr/bin/env python3
"""Deterministic stranded, six-time-point reads for end-to-end execution testing."""
import csv
import gzip
import math
from pathlib import Path
import random
import sys

root = Path(sys.argv[1])
root.mkdir(parents=True, exist_ok=True)
rng = random.Random(99517)
sequences = {name: ''.join(rng.choices('ACGT', k=length)) for name, length in [('chr1h', 60000), ('chr2Lf', 8000), ('chrIy', 8000)]}
with (root / 'fixture.fa').open('w') as handle:
    for name, seq in sequences.items():
        handle.write(f'>{name}\n{seq}\n')
genes = []
with (root / 'fixture.gtf').open('w') as handle:
    for chrom, number in [('chr1h', 48), ('chr2Lf', 6), ('chrIy', 6)]:
        suffix = chrom[-1]
        for i in range(number):
            start = i * 1000 + 100
            strand = '+' if i % 2 == 0 else '-'
            gene, transcript = f'GENE{i:03}{suffix}', f'TX{i:03}{suffix}'
            genes.append((chrom, i, start, strand))
            for j, (a, b) in enumerate([(start, start+199), (start+400, start+599)]):
                exon = j+1 if strand == '+' else 2-j
                attrs = f'gene_id "{gene}"; transcript_id "{transcript}"; exon_number {exon}; exon_id "TX{i:03}.{exon}{suffix}"; gene_name "{gene}";'
                handle.write(f'{chrom}\trefGene\texon\t{a}\t{b}\t.\t{strand}\t.\t{attrs}\n')
raw = root / 'RawSequencingData/HEK293_R1'
raw.mkdir(parents=True, exist_ok=True)
times = [1,2,4,8,12,24]
with (root / 'samples.tsv').open('w') as handle:
    writer = csv.writer(handle, delimiter='\t')
    writer.writerow(['sample','time_hours'])
    for t in times:
        sample = f'HEK293_R1_{t:02}'
        writer.writerow([sample,t])
        counter = 0
        with gzip.open(raw / (sample+'.fastq.gz'), 'wt') as fastq:
            for chrom, i, start, strand in genes:
                human = chrom.endswith('h')
                exonic = round(180 * (1 - math.exp(-math.log(2) * t / (1+i%12)))) if human else 80
                # Four distinct intron dynamics, with a well-behaved early plateau.
                shape = [1, 0.05 + t/24, 0.05 + (t/24)**2, 0.05 + (t/24)**3][i%4]
                intronic = round((65+i) * shape) if human else 20
                for kind, nreads in [('exon',exonic), ('intron',intronic)]:
                    for k in range(nreads):
                        pos = start-1 + (0 if kind=='exon' else 200) + ((k*13) % 151)
                        read = sequences[chrom][pos:pos+50]
                        if strand == '+':
                            read = read.translate(str.maketrans('ACGT','TGCA'))[::-1]
                        counter += 1
                        fastq.write(f'@{sample}_{counter}\n{read}\n+\n'+ 'I'*50+'\n')
print('Synthetic fixture created:', root)
