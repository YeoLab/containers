################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:latest

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:latest"
LABEL version="1"
LABEL software="R, Python3"
LABEL software.version="1.32"
LABEL about.summary="This package implements functions to retrieve the nearest genes around the peak, annotate genomic region of the peak, statstical methods for estimate the significance of overlap among ChIP peak data sets, and incorporate GEO database for user to compare the own dataset with those deposited in database."
LABEL about.home="https://github.com/yeolab/containers"
LABEL about.documentation=""
LABEL about.license="Artistic-2.0"
LABEL about.tags=""
LABEL about.publication="https://doi.org/10.1093/bioinformatics/btv145"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Bioconda data-package hooks need raw yq scalar output and a single R
# architecture. Without those, current Conda transactions can attempt to load
# a temporary "R.c~" executable as a second architecture.
RUN for attempt in 1 2 3; do \
      mamba install -y -c bioconda -c conda-forge bioconductor-data-packages && break; \
      if [ "$attempt" = 3 ]; then exit 1; fi; \
      mamba clean --all -y; \
    done && \
    sed -i \
      -e 's/yq /yq -r /g' \
      -e 's/R CMD INSTALL /R CMD INSTALL --no-multiarch /' \
      /opt/conda/bin/installBiocDataPackage.sh

# Install additional R packages from conda-forge using mamba
RUN for attempt in 1 2 3; do \
      mamba install -y -c bioconda -c r -c conda-forge -c anaconda --file /tmp/conda-packages.txt && break; \
      if [ "$attempt" = 3 ]; then exit 1; fi; \
      mamba clean --all -y; \
    done

# Older Bioconda data packages ship package-specific post-link scripts that
# current mamba versions do not reliably execute. Run the required hooks in
# dependency order, with the same single-architecture R workaround, then
# confirm ChIPseeker can load.
RUN set -eux; \
    for hook in \
      /opt/conda/bin/.bioconductor-genomeinfodbdata-post-link.sh \
      /opt/conda/bin/.bioconductor-go.db-post-link.sh \
      /opt/conda/bin/.bioconductor-do.db-post-link.sh \
      /opt/conda/bin/.bioconductor-org.hs.eg.db-post-link.sh \
      /opt/conda/bin/.bioconductor-txdb.hsapiens.ucsc.hg19.knowngene-post-link.sh \
      /opt/conda/bin/.bioconductor-txdb.hsapiens.ucsc.hg38.knowngene-post-link.sh \
      /opt/conda/bin/.bioconductor-ensdb.hsapiens.v75-post-link.sh; do \
      sed -i -e '2i set -e' -e 's/R CMD INSTALL /R CMD INSTALL --no-multiarch /' "$hook"; \
      PREFIX=/opt/conda PKG_NAME=bioconductor-data PKG_VERSION=manual PKG_BUILDNUM=0 bash "$hook"; \
    done; \
    Rscript -e 'library(ChIPseeker); stopifnot(as.character(packageVersion("ChIPseeker")) == "1.32.0")'

RUN Rscript -e 'IRkernel::installspec(name = "r-chipseeker-1.32", displayname = "R (ChIPseeker-1.32)", user = FALSE)'

USER $NB_UID
