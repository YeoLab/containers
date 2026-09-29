FROM bioconductor/bioconductor_docker:RELEASE_3_23@sha256:821dbf9ac119eac41f177531c7ca8fc7084c99c04eb218a1aa7f52cb63bad5d9

LABEL software="Bambu" \
      software.version="3.14.0" \
      about.summary="Long-read transcript discovery and quantification" \
      about.url="https://bioconductor.org/packages/3.23/bioc/html/bambu.html" \
      about.license="GPL-3.0-only" \
      about.tags="Genomics,long-read-RNA,isoform-quantification"

RUN Rscript -e 'BiocManager::install("bambu", ask = FALSE, update = FALSE)'

COPY verify.R /tmp/verify.R
RUN Rscript /tmp/verify.R && rm /tmp/verify.R

WORKDIR /work
CMD ["R"]
