 
FROM jupyter/datascience-notebook:hub-2.2.2
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

USER $NB_USER
RUN R -e "dir.create(Sys.getenv('R_LIBS_USER'),recursive=TRUE)"
RUN R -e "install.packages('groundhog',repos = 'http://cran.us.r-project.org')"
RUN R -e "groundhog::set.groundhog.folder('~/R_groundhog/')"
RUN R -e "groundhog::groundhog.library(c('tidyverse', 'VGAM', 'viridis', 'ggrepel', 'RColorBrewer', 'Rtsne', 'ggupset', 'ggdendro', 'cowplot', 'BiocManager'), '2022-03-11', force.install=TRUE)" \
    && R -q -e "BiocManager::install(c('GenomicRanges','fgsea','rtracklayer'))"

