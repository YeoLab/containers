################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="umicollapse"
LABEL software.version="1.0.0"
LABEL about.summary="Accelerating the deduplication and collapsing process for reads with Unique Molecular Identifiers (UMI)."
LABEL about.home="https://github.com/Daniel-Liu-c0deb0t/UMICollapse"
LABEL about.documentation="https://github.com/Daniel-Liu-c0deb0t/UMICollapse"
LABEL about.license_file="https://github.com/Daniel-Liu-c0deb0t/UMICollapse/blob/master/LICENSE"
LABEL about.license="MIT"
LABEL about.tags="Genomics"
  
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

COPY conda-packages.txt /tmp/conda-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

USER $NB_UID
