FROM bioconductor/bioconductor_docker:RELEASE_3_23@sha256:821dbf9ac119eac41f177531c7ca8fc7084c99c04eb218a1aa7f52cb63bad5d9

LABEL software="DESeq2" \
      software.version="1.52.0" \
      about.summary="Differential gene expression analysis based on the negative binomial distribution" \
      about.url="https://bioconductor.org/packages/3.23/bioc/html/DESeq2.html" \
      about.license="LGPL-3.0-or-later" \
      about.tags="Genomics,RNA-seq,differential-expression"

RUN Rscript -e 'BiocManager::install("DESeq2", ask = FALSE, update = FALSE)'

COPY verify.R /tmp/verify.R
RUN Rscript /tmp/verify.R && rm /tmp/verify.R

CMD ["R"]
