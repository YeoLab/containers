################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="R"
LABEL software.version="1.0.0"
LABEL about.summary="Contains essential software packages for analyzing electrophysiology-type data"
LABEL about.home="https://hub.docker.com/repository/docker/brianyee/ephys-essentials"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license="GPL-3"
LABEL about.tags="Electrophysiology"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge --file /tmp/conda-packages.txt

USER $NB_UID

