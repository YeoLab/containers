#!/usr/bin/env python3
"""Biological invariants of representative-transcript and overlap filtering."""
from pathlib import Path
import subprocess
import tempfile

with tempfile.TemporaryDirectory() as temp:
    root = Path(temp)
    gtf = root / 'input.gtf'
    rows = []
    for gene, tx, strand, intervals in [
        ('A', 'AS', '+', [(101,150),(301,350)]),
        ('A', 'AL', '+', [(101,200),(301,400)]),
        ('B', 'B', '+', [(181,220),(501,550)]),
        ('C', 'C', '-', [(101,200),(301,400)]),
    ]:
        for i,(a,b) in enumerate(intervals):
            n = i+1 if strand=='+' else 2-i
            attrs = f'gene_id "{gene}h"; transcript_id "{tx}h"; exon_number {n}; exon_id "{tx}.{n}h"; gene_name "{gene}h";'
            rows.append(f'chr1h\trefGene\texon\t{a}\t{b}\t.\t{strand}\t.\t{attrs}\n')
    gtf.write_text(''.join(rows))
    subprocess.run(['Rscript','/opt/DRUID/process_GTF.R',str(gtf)], check=True)
    def features(suffix):
        rows = [x.split('\t') for x in (root / ('input.'+suffix+'.gtf')).read_text().splitlines() if not x.startswith('#')]
        return {(int(r[3]),int(r[4]),r[6]) for r in rows}
    assert features('exons') == {(101,200,'+'),(301,400,'+'),(181,220,'+'),(501,550,'+'),(101,200,'-'),(301,400,'-')}
    assert features('exons.no') == {(301,400,'+'),(501,550,'+'),(101,200,'-'),(301,400,'-')}
    assert features('introns') == {(201,300,'-')}
print('PASS: longest transcript, exon overlaps, intron exclusion, and strand handling')
