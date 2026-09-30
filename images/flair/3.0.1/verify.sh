#!/usr/bin/env bash
set -euo pipefail

[[ "$(flair --version)" == "FLAIR 3.0.1" ]]
for command in minimap2 samtools bedtools gtf_to_bed bed_to_gtf; do
  command -v "$command" >/dev/null
done

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
printf 'chr1\t1\t100\ttranscript1\t0\t+\t1\t100\t0\t1\t99,\t0,\n' > "$work/input.bed"
bed_to_gtf --force "$work/input.bed" > "$work/output.gtf"
test -s "$work/output.gtf"
grep -q 'transcript_id "transcript1"' "$work/output.gtf"
echo "FLAIR 3.0.1 smoke test passed"
