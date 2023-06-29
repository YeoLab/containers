################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="Visual"
LABEL software.version="1.0.0"
LABEL about.summary="tools for visualizations"
LABEL about.tags="Plot visualizations"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt
RUN conda update conda;
RUN conda install -y -c bioconda ensdb.hsapiens.v79

USER $NB_UID