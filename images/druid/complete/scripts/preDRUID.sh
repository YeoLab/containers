#!/usr/bin/env bash
set -euo pipefail
: "${GTF_NO_EXON:?}" "${GTF_INTRON:?}" "${GENOME_SIZES:?}" "${BAM_PATH:?}"
export LC_ALL=C
mkdir -p "${TMPDIR:-/tmp}"
scratch=$(mktemp -d "${TMPDIR:-/tmp}/predruid.XXXXXX")
trap 'rm -rf "$scratch"' EXIT
for type in exon intron; do
    input=$GTF_NO_EXON
    [[ $type == intron ]] && input=$GTF_INTRON
    awk '$7=="-"' "$input" | sort -k1,1 -k4,4n > "$scratch/$type.neg.gtf"
    awk '$7=="+"' "$input" | sort -k1,1 -k4,4n > "$scratch/$type.pos.gtf"
done
mkdir -p intersect
shopt -s nullglob
bams=("$BAM_PATH"/*.bam)
(( ${#bams[@]} > 0 )) || { echo 'No BAM files found' >&2; exit 1; }
for bam in "${bams[@]}"; do
    base=$(basename "$bam" .bam)
    samtools view -h "$bam" | awk '/^@/ || /\tNH:i:1(\t|$)/' | samtools view -b -o "$scratch/unique.bam" -
    bedtools genomecov -ibam "$scratch/unique.bam" -bg -split -strand - | sort -k1,1 -k2,2n > "$scratch/neg.bg"
    bedtools genomecov -ibam "$scratch/unique.bam" -bg -split -strand + | sort -k1,1 -k2,2n > "$scratch/pos.bg"
    for type in exon intron; do
        for strand in neg pos; do
            other=pos
            [[ $strand == pos ]] && other=neg
            bedtools intersect -a "$scratch/$type.$other.gtf" -b "$scratch/$strand.bg" -wo -sorted -g "$GENOME_SIZES" > "$scratch/overlap.tsv"
            python3 "${DRUID_HOME:-/opt/DRUID}/coverage.py" "$scratch/overlap.tsv" > "intersect/${base}_${type}_${strand}.csv"
        done
    done
done
