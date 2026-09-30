#!/usr/bin/env bash
set -euo pipefail

[[ "$(oarfish --version)" == "oarfish 0.10.3" ]]
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT
sequence="ACGTACGTTGCAAGTCGATCGTACGATGCTAGCTAGGCTAACGTTGCACTGATCGTAGCTAGCATCGATGCTAGCTACGATCGTACGTTAGC"
printf '>tx1\n%s%s%s%s%s%s\n' "$sequence" "$sequence" "$sequence" "$sequence" "$sequence" "$sequence" > "$work/transcripts.fa"
oarfish --only-index --annotated "$work/transcripts.fa" --index-out "$work/index" --seq-tech pac-bio-hifi
test -s "$work/index"
echo "Oarfish 0.10.3 smoke test passed"
