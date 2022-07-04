################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="R, Python3"
LABEL software.version="1.2.1"
LABEL about.summary="Container with some spatial transcriptomics + single cell RNAseq software installed"
LABEL about.home="https://github.com/yeolab/containers"
LABEL about.documentation=""
LABEL about.tags=""

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install python packages from pip
RUN python3 -m pip install -r /tmp/python-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge -c anaconda --file /tmp/conda-packages.txt

RUN cd /opt && \
  wget https://github.com/kharchenkolab/Baysor/releases/download/v0.5.1/baysor_ubuntu-latest_x64_build.zip && \
  unzip /opt/baysor_ubuntu-latest_x64_build.zip && \
  rm /opt/baysor_ubuntu-latest_x64_build.zip

RUN cd /tmp && \
  git clone https://github.com/LucasESBS/scoreCT && \
  cd /tmp/scoreCT && \
  python setup.py install

RUN mkdir -p /content/sctoolkit/sctoolkit/ && touch /content/sctoolkit/sctoolkit/__init__.py

COPY proportions.py /content/sctoolkit/sctoolkit/proportions.py

COPY cellranger-7.0.0.tar.gz /opt/cellranger-7.0.0.tar.gz

RUN cd /opt && tar -xvf /opt/cellranger-7.0.0.tar.gz && rm /opt/cellranger-7.0.0.tar.gz

COPY cellranger-arc-2.0.1.tar.gz /opt/cellranger-arc-2.0.1.tar.gz

RUN cd /opt && tar -xvf /opt/cellranger-arc-2.0.1.tar.gz && rm /opt/cellranger-arc-2.0.1.tar.gz

ENV PATH=/opt/cellranger-arc-2.0.1/bin:/opt/cellranger-7.0.0:$PATH

ENV NUMBA_CACHE_DIR=/home/jovyan

USER $NB_UID

