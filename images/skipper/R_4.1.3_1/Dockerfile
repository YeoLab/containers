FROM jupyter/r-notebook:r-4.1.3

USER root

ENV DEBIAN_FRONTEND=non-interactive

RUN apt-get update && apt-get install -y \
    libgcc-s1 \
    curl \
    libgomp1 \
    libbz2-dev \
    libncurses5 \
    libreadline8 \
    libtk8.6 \
    liblzma5 \
    libclang-dev \
    zlib1g \
    libcurl4-openssl-dev \
    libxml2 \
    && rm -rf /var/lib/apt/lists/*

ENV R_LIBS=/home/jovyan/R/x86_64-conda-linux-gnu-library/4.1

RUN Rscript -e "dir.create(Sys.getenv('R_LIBS_USER'),recursive=TRUE)"

RUN Rscript -e "install.packages('groundhog',repos = 'http://cran.us.r-project.org')"

RUN Rscript -e "groundhog::set.groundhog.folder('~/R_groundhog/')"

RUN Rscript -e "groundhog::groundhog.library(c('tidyverse', 'VGAM', 'viridis', 'ggrepel', 'RColorBrewer', 'Rtsne', 'ggupset', 'ggdendro', 'cowplot', 'BiocManager'), '2022-03-11', force.install=TRUE)" \
    && R -q -e "BiocManager::install(c('GenomicRanges','fgsea','rtracklayer'))"

# ENV R_LIBS=/home/jovyan/R/x86_64-conda-linux-gnu-library/4.1

USER $NB_UID

