################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="mageck"
LABEL software.version="0.5.9.5"
LABEL about.summary="Model-based Analysis of Genome-wide CRISPR-Cas9 Knockout"
LABEL about.url="https://sourceforge.net/projects/mageck/"
LABEL about.license="BSD"
LABEL about.license_file="https://github.com/theislab/scarches/blob/master/LICENSE"
LABEL about.publication="https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0554-4"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

USER $NB_UID
