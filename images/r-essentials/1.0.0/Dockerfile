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
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github("mojaveazure/seurat-disk")'
RUN Rscript -e 'devtools::install_github("satijalab/seurat-data")'
USER $NB_UID
