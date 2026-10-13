FROM bioconductor/bioconductor_docker:RELEASE_3_23@sha256:821dbf9ac119eac41f177531c7ca8fc7084c99c04eb218a1aa7f52cb63bad5d9

LABEL software="Isosceles" \
      software.version="0.2.1" \
      about.summary="Single-cell and bulk long-read isoform analysis" \
      about.url="https://github.com/Genentech/Isosceles" \
      about.license="GPL-3.0-or-later" \
      about.tags="Genomics,long-read-RNA,single-cell,isoforms"

ARG ISOSCELES_COMMIT=a009507e6c5391f697cf2e622f2cccc3b45f1e79

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/Genentech/Isosceles.git /opt/Isosceles \
    && cd /opt/Isosceles \
    && git checkout "$ISOSCELES_COMMIT" \
    # Bioconductor 3.20+ moved makeTxDbFromGFF from GenomicFeatures to txdbmaker.
    && sed -i 's/GenomicFeatures::makeTxDbFromGFF/txdbmaker::makeTxDbFromGFF/' R/gtf_to_intron_bed.R R/prepare_reference_annotations.R \
    && sed -i 's/^\(    GenomicFeatures (>= 1.48.3),\)$/\1\n    txdbmaker,/' DESCRIPTION \
    && grep -q '^    txdbmaker,$' DESCRIPTION

# Install required packages only; upstream Suggests include vignette and
# plotting extras that are not needed to load or run the package.
RUN Rscript -e 'BiocManager::install(c("SingleCellExperiment", "rlang", "assertthat", "magrittr", "tibble", "tidyselect", "dplyr", "tidyr", "forcats", "glue", "digest", "Rcpp", "Matrix", "BiocParallel", "BiocNeighbors", "S4Vectors", "BiocGenerics", "Biostrings", "BSgenome", "GenomeInfoDb", "IRanges", "GenomicRanges", "Rsamtools", "GenomicAlignments", "rtracklayer", "GenomicFeatures", "txdbmaker", "SummarizedExperiment", "DEXSeq", "igraph", "scuttle", "scran", "fastmatch", "pheatmap", "ggbio", "ggplot2", "biovizBase", "RcppArmadillo"), ask = FALSE, update = FALSE)' \
    && R CMD INSTALL /opt/Isosceles \
    && Rscript -e 'library(Isosceles); stopifnot(as.character(packageVersion("Isosceles")) == "0.2.1")' \
    && Rscript -e 'suppressPackageStartupMessages(library(Isosceles)); f <- function(x) system.file("extdata", x, package = "Isosceles"); bams <- c(Sample = f("bulk_rnaseq.bam")); bp <- bam_to_read_structures(bam_files = bams); tx <- prepare_transcripts(gtf_file = f("bulk_rnaseq.gtf"), genome_fasta_file = f("bulk_rnaseq.fa"), bam_parsed = bp); se <- tcc_to_transcript(bam_to_tcc(bam_files = bams, transcript_data = tx)); stopifnot(nrow(se) > 0)'

WORKDIR /work
CMD ["R"]
