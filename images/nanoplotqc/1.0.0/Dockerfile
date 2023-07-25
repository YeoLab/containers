################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="nanoplotqc"
LABEL software.version="v1.32.1"
LABEL about.summary="Nanoplot software and dependencies"
LABEL about.url="https://github.com/wdecoster/NanoPlot/tree/master"
LABEL about.license=""
LABEL about.license_file="https://github.com/wdecoster/NanoPlot/blob/master/LICENSE"
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

# COPY apt-packages.txt /tmp/apt-packages.txt
COPY nanoplotqc.yml /tmp/nanoplotqc.yml

# Install additional R packages from conda-forge using mamba
RUN conda env create -f /tmp/nanoplotqc.yml

SHELL ["conda","run","-n","nanoplotqc","/bin/bash","-c"]

USER $NB_UID

ENV PATH /opt/conda/envs/nanoplotqc/bin/:$PATH