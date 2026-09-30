#!/usr/bin/env bash
set -euo pipefail

[[ "$(kallisto version)" == "kallisto, version 0.52.0" ]]
work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

sequence="ACGTACGTTGCAAGTCGATCGTACGATGCTAGCTAGGCTAACGTTGCACTGATCGTAGCTAGCATCGATGCTAGCTACGATCGTACGTTAGC"
printf '>tx1\n%s%s%s\n' "$sequence" "$sequence" "$sequence" > "$work/transcripts.fa"
printf '@read1\n%s\n+\n%s\n' "$sequence" "$(printf '%*s' "${#sequence}" '' | tr ' ' I)" > "$work/reads.fq"
kallisto index -k 63 -i "$work/transcripts.idx" "$work/transcripts.fa"
kallisto quant --single -l "${#sequence}" -s 10 -i "$work/transcripts.idx" -o "$work/quant" "$work/reads.fq"
test -s "$work/quant/abundance.tsv"
grep -q '^tx1' "$work/quant/abundance.tsv"
echo "lr-kallisto 0.52.0 smoke test passed"
