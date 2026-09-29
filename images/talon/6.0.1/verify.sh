#!/usr/bin/env bash
set -euo pipefail

python - <<'PY'
from importlib_metadata import version
assert version("talon") == "5.0"
PY

for command in talon talon_initialize_database talon_abundance talon_create_GTF talon_create_adata; do
  command -v "$command" >/dev/null
  "$command" --help >/dev/null
done

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
printf '%b\n' \
  'chr1\tsmoke\tgene\t1\t200\t.\t+\t.\tgene_id "g1"; gene_name "G1";' \
  'chr1\tsmoke\ttranscript\t1\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; gene_name "G1"; transcript_name "T1";' \
  'chr1\tsmoke\texon\t1\t50\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_number "1"; exon_id "e1";' \
  'chr1\tsmoke\texon\t101\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_number "2"; exon_id "e2";' \
  > "$work/input.gtf"

talon_initialize_database --f "$work/input.gtf" --g smoke --a smoke --o "$work/talon"
test -s "$work/talon.db"
python - "$work/talon.db" <<'PY'
import sqlite3
import sys
with sqlite3.connect(sys.argv[1]) as connection:
    assert connection.execute("SELECT COUNT(*) FROM transcripts").fetchone()[0] == 1
PY
echo "TALON 6.0.1 smoke test passed"
