#!/usr/bin/env bash
set -euo pipefail
root=$(realpath "${1:-/work}")
mkdir -p "$root"
fixture=$(mktemp -d "$root/smoke.XXXXXX")
export TMPDIR="$fixture/tmp"
mkdir -p "$TMPDIR"
python3 /opt/tests/check_coverage.py
python3 /opt/tests/check_predruid.py
python3 /opt/tests/check_annotations.py
python3 /opt/tests/make_fixture.py "$fixture"
druid reference --work "$fixture" --fasta "$fixture/fixture.fa" --gtf "$fixture/fixture.gtf" --small-genome --threads 2
druid analyze --work "$fixture" --manifest "$fixture/samples.tsv" --threads 2
Rscript /opt/tests/check_results.R "$fixture"
test -s "$fixture/Analysis/HEK293_R1/DRUID.replicate.1.heatmap.DRUID.pdf"
# Also exercise UCSC converters using a small real genePred table and 2bit genome.
curl -fL --retry 3 https://hgdownload.soe.ucsc.edu/goldenPath/sacCer3/database/sgdGene.txt.gz -o "$fixture/sgdGene.txt.gz"
python3 - "$fixture" <<'PYCODE'
import sys
from pathlib import Path
sys.path.insert(0, '/opt/workflow')
from druid import unpack_genepred
root = Path(sys.argv[1])
unpack_genepred(root / 'sgdGene.txt.gz', root / 'sgdGene.gp', 'sgdGene')
PYCODE
genePredToGtf -utr file "$fixture/sgdGene.gp" "$fixture/sgdGene.gtf"
test -s "$fixture/sgdGene.gtf"
curl -fL --retry 3 https://hgdownload.soe.ucsc.edu/goldenPath/sacCer3/bigZips/sacCer3.2bit -o "$fixture/sacCer3.2bit"
twoBitToFa "$fixture/sacCer3.2bit" "$fixture/sacCer3.fa"
test -s "$fixture/sacCer3.fa"
python3 - "$fixture" <<'PYCODE'
import sys
from pathlib import Path
sys.path.insert(0, '/opt/workflow')
from druid import label_reference
root = Path(sys.argv[1])
label_reference(root / 'sacCer3.fa', root / 'sgdGene.gtf', 'y', False, root / 'yeast.fa', root / 'yeast.gtf')
PYCODE
Rscript /opt/DRUID/process_GTF.R "$fixture/yeast.gtf"
test -s "$fixture/yeast.introns.gtf"
echo "PASS: complete workflow and UCSC converters. Results: $fixture"
