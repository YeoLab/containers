################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="isoquant"
LABEL software.version="v3.3"
LABEL about.summary="Software for completing quantification of isoforms with long-read sequencing"
LABEL about.url="https://github.com/ablab/IsoQuant"
LABEL about.license=""
LABEL about.license_file="https://github.com/ablab/IsoQuant/blob/master/LICENSE"
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

# COPY apt-packages.txt /tmp/apt-packages.txt
COPY isoquant.yml /tmp/isoquant.yml

# Install additional R packages from conda-forge using mamba
RUN conda env create -f /tmp/isoquant.yml

SHELL ["conda","run","-n","isoquant","/bin/bash","-c"]

USER $NB_UID

ENV PATH /opt/conda/envs/isoquant/bin/:$PATH
