################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="R, Python3"
LABEL software.version="1.32"
LABEL about.summary="This package implements functions to retrieve the nearest genes around the peak, annotate genomic region of the peak, statstical methods for estimate the significance of overlap among ChIP peak data sets, and incorporate GEO database for user to compare the own dataset with those deposited in database."
LABEL about.home="https://github.com/yeolab/containers"
LABEL about.documentation=""
LABEL about.license="Artistic-2.0"
LABEL about.tags=""
LABEL about.publication="https://doi.org/10.1093/bioinformatics/btv145"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge -c anaconda --file /tmp/conda-packages.txt

RUN Rscript -e 'IRkernel::installspec(name = "r-chipseeker-1.32", displayname = "R (ChIPseeker-1.32)", user = FALSE)'

USER $NB_UID

