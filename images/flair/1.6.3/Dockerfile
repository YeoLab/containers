################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="flair"
LABEL software.version="1.6.3"
LABEL about.summary="Correction, isoform definition, and alternative splicing analysis of noisy reads (ONT and PacBio)."
LABEL about.url="https://github.com/BrooksLabUCSC/flair"
LABEL about.license_file="https://github.com/BrooksLabUCSC/flair/blob/master/LICENSE.txt"
LABEL about.publication="https://doi.org/10.1038/s41467-020-15171-6"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

USER $NB_UID
