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
# FLAIR's transcriptome filter needs MD tags from minimap2 --MD.
[[ "$(minimap2 --version)" == 2.30-* ]]
python3 -c "import random; random.seed(1); s=''.join(random.choice('ACGT') for _ in range(500)); open('$work/ref.fa','w').write('>ref\\n'+s+'\\n'); open('$work/read.fa','w').write('>read\\n'+s[50:450]+'\\n')"
minimap2 -a --MD "$work/ref.fa" "$work/read.fa" 2>/dev/null | grep -v '^@' | grep -q $'\tMD:Z:'
echo "FLAIR 3.0.1 smoke test passed"
