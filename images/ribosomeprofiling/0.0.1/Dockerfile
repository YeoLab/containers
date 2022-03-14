################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="ribosomeprofiling"
LABEL software.version="0.0.1"
LABEL about.summary="R packages Babel and Xtail for ribosome profiling analysis"
LABEL about.xtail.url="https://github.com/xryanglab/xtail"
LABEL about.xtail.license="GPL-3"
LABEL about.xtail.license_file="https://github.com/xryanglab/xtail/blob/master/LICENSE"
LABEL about.xtail.publication="https://doi.org/10.1016/j.cell.2021.04.048"
LABEL about.babel.url="https://github.com/olshena/babel"
LABEL about.babel.publication="https://doi.org/10.1093/bioinformatics/btt533"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c r -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github("FelixErnst/xtail-1")'  # https://github.com/FelixErnst/xtail-1 for R-4.0+
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org"); BiocManager::install("babel")'

USER $NB_UID
