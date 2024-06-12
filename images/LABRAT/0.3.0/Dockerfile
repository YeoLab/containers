################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="labrat"
LABEL software.version="0.3.0"
LABEL about.summary="A package to quantify changes in alternative polyadenylation isoform abundance using RNAseq data"
LABEL about.url="https://github.com/TaliaferroLab/LABRAT"
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/TaliaferroLab/LABRAT?tab=MIT-1-ov-file#readme"
LABEL about.publication="https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-021-07781-1"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

USER $NB_UID
