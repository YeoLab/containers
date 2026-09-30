#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
from importlib.metadata import version
assert version("cerberus") == "1.1"
import cerberus.cerberus
PY
python -m pip check
cerberus --help >/dev/null

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
printf '%b\n' \
  'chr1\tsmoke\tgene\t1\t200\t.\t+\t.\tgene_id "g1"; gene_name "G1";' \
  'chr1\tsmoke\ttranscript\t1\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; gene_name "G1"; transcript_name "T1";' \
  'chr1\tsmoke\texon\t1\t50\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_number "1";' \
  'chr1\tsmoke\texon\t101\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_number "2";' \
  > "$work/input.gtf"

cerberus gtf_to_bed --gtf "$work/input.gtf" --mode tss -o "$work/tss.bed"
cerberus gtf_to_ics --gtf "$work/input.gtf" -o "$work/ics.tsv"
test -s "$work/tss.bed"
test -s "$work/ics.tsv"
grep -q 'g1_1' "$work/ics.tsv"
echo "Cerberus 1.1 smoke test passed"
