################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software=""
LABEL software.version="0.1.8"
LABEL about.summary="Bioinformatic tool for Splice site Strength Estimation using RNA-seq"
LABEL about.home="https://github.com/CraigIDent/SpliSER"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Genomics"
  
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

COPY conda-packages.txt /tmp/conda-packages.txt
# Install additional packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt
RUN cd /opt && git clone https://github.com/griffithlab/regtools && \
    cd regtools/ && \
    mkdir build && \
    cd build/ && \
    cmake .. && \
    make
RUN cd /opt && git clone https://github.com/CraigIDent/SpliSER
ENV PATH /opt/regtools/build:/opt/SpliSER/:$PATH
USER $NB_UID
