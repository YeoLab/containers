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
  'chr1\tsmoke\texon\t101\t150\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_number "2";' \
  'chr1\tsmoke\texon\t171\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t1"; exon_number "3";' \
  'chr1\tsmoke\ttranscript\t1\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t2"; gene_name "G1"; transcript_name "T2";' \
  'chr1\tsmoke\texon\t1\t30\t.\t+\t.\tgene_id "g1"; transcript_id "t2"; exon_number "1";' \
  'chr1\tsmoke\texon\t101\t150\t.\t+\t.\tgene_id "g1"; transcript_id "t2"; exon_number "2";' \
  'chr1\tsmoke\texon\t171\t200\t.\t+\t.\tgene_id "g1"; transcript_id "t2"; exon_number "3";' \
  > "$work/input.gtf"

cerberus gtf_to_bed --gtf "$work/input.gtf" --mode tss -o "$work/tss.bed"
cerberus gtf_to_ics --gtf "$work/input.gtf" -o "$work/ics.tsv"
test -s "$work/tss.bed"
test -s "$work/ics.tsv"
grep -q 'g1_1' "$work/ics.tsv"

# Full reference build and annotation from the reference plus a long-read GTF
# with a novel intron chain. The long-read GTF carries a 'source' attribute like
# TALON's, which must not leak into replace_gtf_ids' output.
printf '%b\n' \
  'chr1\tlr\tgene\t1\t200\t.\t+\t.\tgene_id "g1"; gene_name "G1"; source "TALON";' \
  'chr1\tlr\ttranscript\t1\t200\t.\t+\t.\tgene_id "g1"; transcript_id "n1"; gene_name "G1"; transcript_name "N1"; source "TALON";' \
  'chr1\tlr\texon\t1\t50\t.\t+\t.\tgene_id "g1"; transcript_id "n1"; exon_number "1";' \
  'chr1\tlr\texon\t171\t200\t.\t+\t.\tgene_id "g1"; transcript_id "n1"; exon_number "2";' \
  > "$work/lr.gtf"
for g in input lr; do
  cerberus gtf_to_bed --gtf "$work/$g.gtf" --mode tss -o "$work/${g}_tss.bed"
  cerberus gtf_to_bed --gtf "$work/$g.gtf" --mode tes -o "$work/${g}_tes.bed"
  cerberus gtf_to_ics --gtf "$work/$g.gtf" -o "$work/${g}_ics.tsv"
done
for m in tss tes; do
  printf '%s\n' "$work/input_$m.bed,True,True,ref" "$work/lr_$m.bed,True,False,lr" > "$work/agg_$m.csv"
  cerberus agg_ends --input "$work/agg_$m.csv" --mode $m -o "$work/agg_$m.bed"
done
printf '%s\n' "$work/input_ics.tsv,True,ref" "$work/lr_ics.tsv,False,lr" > "$work/agg_ics.csv"
cerberus agg_ics --input "$work/agg_ics.csv" -o "$work/agg_ics.tsv"
cerberus write_reference --tss "$work/agg_tss.bed" --tes "$work/agg_tes.bed" --ics "$work/agg_ics.tsv" -o "$work/ref.h5"
cerberus annotate_transcriptome --gtf "$work/input.gtf" --h5 "$work/ref.h5" --source ref -o "$work/annot_ref.h5"
cerberus annotate_transcriptome --gtf "$work/lr.gtf" --h5 "$work/annot_ref.h5" --source lr --gene_source ref -o "$work/annot.h5"
cerberus replace_gtf_ids --h5 "$work/annot.h5" --gtf "$work/lr.gtf" --source lr --update_ends --collapse -o "$work/lr_cerberus.gtf"
awk -F'\t' 'NF != 9 {exit 1}' "$work/lr_cerberus.gtf"
grep -q 'transcript_id "g1\[' "$work/lr_cerberus.gtf"
echo "Cerberus 1.1 smoke test passed"
