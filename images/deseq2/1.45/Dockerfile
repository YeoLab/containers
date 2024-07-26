################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="deseq2"
LABEL software.version="1.45.0"
LABEL about.summary="Differential gene expression analysis based on the negative binomial distribution"
LABEL about.url="https://bioconductor.org/packages/3.16/bioc/html/DESeq2.html"
LABEL about.license="LGPL (>= 3)"
LABEL about.publication="10.1186/s13059-014-0550-8"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
# COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
# RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt
RUN mamba install -y -c bioconda -c conda-forge r-curl r-reticulate r-units r-gmp r-sf
RUN mamba install -y -c bioconda -c conda-forge r-v8 r-ggplot2 r-dplyr r-patchwork r-cowplot r-scales
RUN mamba install -y -c bioconda -c conda-forge r-reshape2 r-future r-readr r-rcolorbrewer r-pheatmap r-plotly r-ggfortify
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install(c("tximportData", "tximeta", "tximport"))'
# RUN mamba install -y -c bioconda -c conda-forge -c r bioconductor-tximport bioconductor-tximportdata=1.30 bioconductor-tximeta
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install(c("BiocParallel", "IHW", "vsn", "pasilla", "DEXSeq", "airway"))'
# RUN mamba install -y -c bioconda -c conda-forge bioconductor-airway bioconductor-biocparallel bioconductor-ihw bioconductor-vsn bioconductor-pasilla bioconductor-dexseq
RUN Rscript -e 'install.packages("devtools", repos = "https://cran.us.r-project.org")'
# RUN Rscript -e 'install.packages("RCurl", repos = "https://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github("mikelove/deseq2", ref = "6e1a3a56f7f6315e4a5ff352a203af26e778f73a")'
RUN Rscript -e 'IRkernel::installspec(name = "deseq2_1.42", displayname = "DESeq2-1.42", user = FALSE)'
#USER $NB_UID
