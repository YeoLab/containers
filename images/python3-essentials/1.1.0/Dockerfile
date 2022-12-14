################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software=""
LABEL software.version="1.0.0"
LABEL about.summary="Contains essential bioinformatics python3 packages, plus other software essential for bioinformatics analysis."
LABEL about.home="https://hub.docker.com/repository/docker/brianyee/python3-essentials"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Bioinformatics"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional conda packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge --file /tmp/conda-packages.txt

RUN cd /opt && \
  git clone https://github.com/yeolab/qtools && \
  cd /opt/qtools/ && \
  pip install . && \
  rm -r /opt/qtools/

USER $NB_UID

