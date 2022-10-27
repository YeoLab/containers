################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software=""
LABEL software.version="1.0.0"
LABEL about.summary="Contains essential software packages for analyzing imaging-type data"
LABEL about.home="https://hub.docker.com/repository/docker/brianyee/imaging-essentials"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Microscopy"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

RUN conda create -c anaconda -n "imaging-essentials" python=3.8 mamba cython

SHELL ["conda", "run", "-n", "imaging-essentials", "/bin/bash", "-c"]

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional conda packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge --file /tmp/conda-packages.txt

RUN mamba install -y -c conda-forge ipykernel
RUN python -m ipykernel install --name imaging-essentials-1 --display-name "Python3 (imaging-essentials)"

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

USER $NB_UID

ENV PATH=/opt/conda/envs/imaging-essentials/bin:$PATH
