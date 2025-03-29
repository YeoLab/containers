################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:python-3.10.11

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:python-3.10.11"
LABEL version="1"
LABEL software="Python3"
LABEL software.version="c7dbd93"
LABEL about.summary="Ben Weisburd's fork of Illumina's spliceai"
LABEL about.home="https://github.com/bw2/SpliceAI"
LABEL about.documentation=""
LABEL about.tags=""

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge -c anaconda --file /tmp/conda-packages.txt

USER $NB_UID
