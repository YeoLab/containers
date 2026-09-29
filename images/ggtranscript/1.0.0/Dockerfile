FROM bioconductor/bioconductor_docker:RELEASE_3_23@sha256:821dbf9ac119eac41f177531c7ca8fc7084c99c04eb218a1aa7f52cb63bad5d9

LABEL software="ggtranscript" \
      software.version="1.0.0" \
      about.summary="Transcript structure and annotation visualization with ggplot2" \
      about.url="https://github.com/dzhang32/ggtranscript" \
      about.license="MIT" \
      about.tags="Genomics,RNA-seq,transcript-visualization"

ARG GGTRANSCRIPT_COMMIT="682a0df688ad242fa262d0b0557bf973dc202787"
ARG GGTRANSCRIPT_SHA256="004fc8d7de0dea3d53c11ac2bb625c649e778b90e0c9ee7b845370282b007001"

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "https://github.com/dzhang32/ggtranscript/archive/${GGTRANSCRIPT_COMMIT}.tar.gz" -o /tmp/ggtranscript.tar.gz \
    && echo "$GGTRANSCRIPT_SHA256  /tmp/ggtranscript.tar.gz" | sha256sum -c -

RUN Rscript -e 'BiocManager::install(c("GenomicRanges", "S4Vectors", "GenomeInfoDb"), ask = FALSE, update = FALSE)' \
    && Rscript -e 'install.packages(c("dplyr", "ggplot2", "magrittr", "rlang", "ggrepel"), repos = "https://cloud.r-project.org")' \
    && R CMD INSTALL /tmp/ggtranscript.tar.gz \
    && rm /tmp/ggtranscript.tar.gz

COPY verify.R /tmp/verify.R
RUN Rscript /tmp/verify.R && rm /tmp/verify.R

WORKDIR /work
CMD ["R"]
