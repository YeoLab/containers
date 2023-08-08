################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="leafcutter"
LABEL software.version="0.2"
LABEL about.summary="Leafcutter quantifies RNA splicing variation using short-read RNA-seq data. The core idea is to leverage spliced reads (reads that span an intron) to quantify (differential) intron usage across samples. The advantages of this approach include"
LABEL about.url="https://davidaknowles.github.io/leafcutter/"
LABEL about.license="GPL3+"
LABEL about.license_file="https://github.com/davidaknowles/leafcutter/blob/master/LICENSE"
LABEL about.publication="http://dx.doi.org/10.1093/bioinformatics/btaa259"
L

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

USER $NB_UID
