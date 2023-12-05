################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="multiqc"
LABEL about.summary="MultiQC searches a given directory for analysis logs and compiles a HTML report. "
LABEL about.url="https://multiqc.info/"
LABEL about.license="GPL-3"
LABEL about.license_file="https://github.com/ewels/MultiQC/blob/master/LICENSE"
LABEL about.publication="http://dx.doi.org/10.1093/bioinformatics/btw354"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

USER $NB_UID
