#!/usr/bin/env python3
"""Python 3 port of DRUID coverage.py, accepting quoted GTF attributes."""
import csv
import re
import sys
import numpy as np

features, info = {}, {}
with open(sys.argv[1], newline='') as handle:
    for row in csv.reader(handle, delimiter='\t'):
        chrom = re.fullmatch(r'(chr[0-9A-Z]+)([hfy])', row[0])
        if not chrom:
            raise ValueError(f'Expected species-suffixed canonical chromosome: {row[0]}')
        attrs = dict(re.findall(r'(\w+)\s+"?([^";]+)"?;', row[8]))
        gene = attrs['gene_id'][:-1]
        exon_id = re.fullmatch(r'(.+)\.(\d+)[hfy]', attrs['exon_id'])
        if not exon_id:
            raise ValueError(f'Expected transcript.number<species> exon_id: {row[8]}')
        transcript, exon = exon_id.groups()
        key = (gene, chrom[2], exon)
        start, end = int(row[3]) - 1, int(row[4])
        if key not in features:
            features[key] = np.zeros(end - start, dtype=np.int32)
            info[key] = [chrom[1], chrom[2], gene, transcript, exon]
        a, b = max(start, int(row[10])) - start, min(end, int(row[11])) - start
        if b - a != int(row[13]):
            raise ValueError(f'Intersection length mismatch: {row}')
        features[key][a:b] += int(row[12])
out = csv.writer(sys.stdout, lineterminator='\n')
out.writerow(['chromosome', 'organism', 'gene', 'transcript', 'exon', 'mean', 'stdev', 'size', 'coverage'])
for key, values in features.items():
    out.writerow(info[key] + [np.mean(values), np.std(values), values.size, np.count_nonzero(values) / values.size])
