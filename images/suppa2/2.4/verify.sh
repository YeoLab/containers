#!/usr/bin/env bash
set -euo pipefail

test "$(python3 /opt/suppa/suppa.py --version)" = "SUPPA 2.4"

python3 - <<'PY'
import matplotlib
import numpy
import pandas
import scipy
import sklearn
import statsmodels
PY

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
cat > "$work/transcripts.gtf" <<'GTF'
chr1	test	exon	1	100	.	+	.	gene_id "gene1"; transcript_id "tx1";
chr1	test	exon	201	300	.	+	.	gene_id "gene1"; transcript_id "tx1";
chr1	test	exon	1	100	.	+	.	gene_id "gene1"; transcript_id "tx2";
chr1	test	exon	151	175	.	+	.	gene_id "gene1"; transcript_id "tx2";
chr1	test	exon	201	300	.	+	.	gene_id "gene1"; transcript_id "tx2";
GTF

python3 /opt/suppa/suppa.py generateEvents \
  -i "$work/transcripts.gtf" \
  -o "$work/events" \
  -f ioi

test -s "$work/events.ioi"
grep -q 'gene1;tx1' "$work/events.ioi"
echo "SUPPA2 2.4 smoke test passed"
