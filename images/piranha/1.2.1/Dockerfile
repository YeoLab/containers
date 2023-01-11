################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="piranha"
LABEL software.version="1.2.1"
LABEL about.summary="Piranha is a peak-caller for CLIP- and RIP-seq data"
LABEL about.url="https://github.com/smithlabcode/piranha"
LABEL about.license="GPL"
LABEL about.license_file="https://github.com/smithlabcode/piranha/blob/master/gpl.txt"
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt
COPY piranha-1.2.1.tar.gz /tmp/piranha-1.2.1.tar.gz
RUN cd /tmp && tar -xvf piranha-1.2.1.tar.gz && \
  cd /tmp/piranha-1.2.1 && \
  ./configure && \
  make && make install

ENV PATH=/tmp/piranha-1.2.1/bin/:$PATH

USER $NB_UID
