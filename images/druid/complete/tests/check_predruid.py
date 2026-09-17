#!/usr/bin/env python3
"""Ensure preDRUID excludes NH=10 reads and selects the opposite read strand."""
import csv
import os
from pathlib import Path
import subprocess
import tempfile
with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    bamdir = root/'BAM'; bamdir.mkdir()
    attrs = 'gene_id "Ah"; transcript_id "TXh"; exon_number 1; exon_id "TX.1h"; gene_name "Ah";'
    (root/'exons.gtf').write_text(f'chr1h\tx\texon\t11\t14\t.\t+\t.\t{attrs}\n')
    (root/'introns.gtf').write_text(f'chr1h\tx\texon\t21\t24\t.\t+\t.\t{attrs}\n')
    (root/'sizes').write_text('chr1h\t100\n')
    sam = '@HD\tVN:1.6\tSO:coordinate\n@SQ\tSN:chr1h\tLN:100\n'
    for i,(flag,pos,nh) in enumerate([(16,11,1),(16,11,10),(0,11,1),(16,21,1),(16,21,10)]):
        sam += f'r{i}\t{flag}\tchr1h\t{pos}\t255\t4M\t*\t0\t0\tAAAA\tIIII\tNH:i:{nh}\n'
    (root/'test.sam').write_text(sam)
    subprocess.run(['samtools','view','-b','-o',str(bamdir/'test.bam'),str(root/'test.sam')],check=True)
    env = dict(os.environ,GTF_NO_EXON=str(root/'exons.gtf'),GTF_INTRON=str(root/'introns.gtf'),
               GENOME_SIZES=str(root/'sizes'),BAM_PATH=str(bamdir),TMPDIR=temp)
    subprocess.run(['bash','/opt/DRUID/preDRUID.sh'],cwd=root,env=env,check=True)
    for feature in ['exon','intron']:
        rows=list(csv.DictReader((root/f'intersect/test_{feature}_neg.csv').open()))
        assert len(rows)==1 and float(rows[0]['mean'])==1 and float(rows[0]['coverage'])==1
        assert not list(csv.DictReader((root/f'intersect/test_{feature}_pos.csv').open()))
print('PASS: exact NH=1 filtering and reverse-stranded coverage')
