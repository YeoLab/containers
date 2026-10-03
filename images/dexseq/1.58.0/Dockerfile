FROM bioconductor/bioconductor_docker:RELEASE_3_23@sha256:821dbf9ac119eac41f177531c7ca8fc7084c99c04eb218a1aa7f52cb63bad5d9

LABEL software="DEXSeq" \
      software.version="1.58.0" \
      about.summary="Inference of differential exon usage in RNA-seq" \
      about.url="https://bioconductor.org/packages/3.23/bioc/html/DEXSeq.html" \
      about.license="GPL-3.0-or-later" \
      about.tags="Genomics,RNA-seq,differential-exon-usage"

RUN Rscript -e 'BiocManager::install("DEXSeq", ask = FALSE, update = FALSE)'

COPY verify.R /tmp/verify.R
RUN Rscript /tmp/verify.R && rm /tmp/verify.R

CMD ["R"]
