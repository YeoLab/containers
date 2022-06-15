################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="R, Python3"
LABEL software.version="1.1.0"
LABEL about.summary="Container with some spatial transcriptomics + single cell RNAseq software installed"
LABEL about.home="https://github.com/yeolab/containers"
LABEL about.documentation=""
LABEL about.tags=""

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

RUN apt-get update

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge -c anaconda --file /tmp/conda-packages.txt

# Install python packages from pip
RUN pip install -r /tmp/python-packages.txt

RUN cd /opt && \
  wget https://github.com/kharchenkolab/Baysor/releases/download/v0.5.1/baysor_ubuntu-latest_x64_build.zip && \
  unzip /opt/baysor_ubuntu-latest_x64_build.zip 
  
ENV NUMBA_CACHE_DIR=/home/jovyan

USER $NB_UID

