################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="r-essentials"
LABEL software.version="1.0.0"
LABEL about.summary="R toolkit for bioinformatics"
LABEL about.url=""
LABEL about.license=""
LABEL about.license_file=""
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY bioconductor-conda-packages.txt /tmp/bioconductor-conda-packages.txt
# COPY r-conda-packages1.txt /tmp/r-conda-packages1.txt
# COPY r-conda-packages2.txt /tmp/r-conda-packages2.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
# RUN mamba install -y -c bioconda -c conda-forge --file /tmp/r-conda-packages1.txt
RUN mamba install -y -c bioconda -c conda-forge r-tidyverse r-reticulate r-units r-ggplot2 r-dplyr r-rtsne r-ggrepel
RUN mamba install -y -c bioconda -c conda-forge r-patchwork r-cowplot r-scales r-reshape2 r-future 
RUN mamba install -y -c bioconda -c conda-forge r-sctransform r-seurat=4.3.0 r-ragg
RUN mamba install -y -c bioconda -c conda-forge r-ggbeeswarm r-rcolorbrewer
# RUN mamba install -y -c bioconda -c conda-forge 
# RUN mamba install -y -c bioconda -c conda-forge --file /tmp/r-conda-packages2.txt
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/bioconductor-conda-packages.txt

RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github("mojaveazure/seurat-disk")'
RUN Rscript -e 'devtools::install_github("satijalab/seurat-data")'
RUN Rscript -e 'devtools::install_github("santiago1234/iCodon")'
RUN Rscript -e 'IRkernel::installspec(name = "ressential_1.0.0", displayname = "R Essentials 1.0.0", user = FALSE)'
USER $NB_UID
