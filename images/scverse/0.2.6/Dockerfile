################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:python-3.10.11

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:python-3.10.11"
LABEL version="1"
LABEL software="R, Python3"
LABEL software.version="1.0.0_spatialdata_0.2.3"
LABEL about.summary="Container with some scverse tools, including spatialdata and bento"
LABEL about.home="https://github.com/yeolab/containers"
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

# Install python packages from pip
COPY python-packages.txt /tmp/python-packages.txt
RUN python3 -m pip install -r /tmp/python-packages.txt

COPY scverse-packages.txt /tmp/scverse-packages.txt
RUN python3 -m pip install --use-deprecated=legacy-resolver -r /tmp/scverse-packages.txt

RUN cd /tmp && \
  git clone https://github.com/LucasESBS/scoreCT && \
  cd /tmp/scoreCT && \
  python setup.py install

RUN mkdir -p /content/sctoolkit/sctoolkit/ && touch /content/sctoolkit/sctoolkit/__init__.py

COPY proportions.py /content/sctoolkit/sctoolkit/proportions.py

COPY xeniumranger-3.1.1.tar.gz /opt/xeniumranger-3.1.1.tar.gz
# RUN python3 -m pip install xarray-datatree==0.0.14 xarray==2024.9.0

RUN cd /opt && tar -xvf /opt/xeniumranger-3.1.1.tar.gz && rm /opt/xeniumranger-3.1.1.tar.gz
COPY _io.py /opt/conda/lib/python3.10/site-packages/bento/io/_io.py
USER $NB_UID

