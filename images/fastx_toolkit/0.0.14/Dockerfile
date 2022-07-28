################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="fastx_toolkit"
LABEL software.version="0.0.14"
LABEL about.summary="FASTQ/A short-reads pre-processing tools"
LABEL about.url="https://hannonlab.cshl.edu/fastx_toolkit/"
LABEL about.license="GNU-3"
LABEL about.license_file="http://hannonlab.cshl.edu/fastx_toolkit/license.html"
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

USER $NB_UID
