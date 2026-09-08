#!/usr/bin/env python3
"""Test overlap coordinates, zero coverage, and feature metadata against hand calculations."""
import csv
import io
import subprocess
import tempfile
import numpy as np
attrs = 'gene_id "Ah"; transcript_id "TXh"; exon_number "1"; exon_id "TX.1h"; gene_name "Ah";'
# Four-base feature; coverage [2, 2, 3, 0]. Input intervals use BED coordinates.
rows = [f'chr1h\tx\texon\t11\t14\t.\t+\t.\t{attrs}\tchr1h\t10\t12\t2\t2',
        f'chr1h\tx\texon\t11\t14\t.\t+\t.\t{attrs}\tchr1h\t12\t13\t3\t1']
with tempfile.NamedTemporaryFile(mode='w') as f:
    f.write('\n'.join(rows)+'\n'); f.flush()
    output = subprocess.check_output(['python3','/opt/DRUID/coverage.py',f.name], text=True)
row = list(csv.DictReader(io.StringIO(output)))[0]
assert row['gene']=='A' and row['transcript']=='TX' and row['size']=='4'
assert float(row['mean'])==1.75 and float(row['coverage'])==0.75
assert np.isclose(float(row['stdev']), np.std([2,2,3,0]))
print('PASS: coverage coordinates and statistics')
