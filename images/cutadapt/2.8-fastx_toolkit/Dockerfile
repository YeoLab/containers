################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:python-3.7.6

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:python-3.7.6"
LABEL version="1"
LABEL software="cutadapt/fastx_toolkit"
LABEL software.version="2.8"
LABEL about.summary="Cutadapt removes adapter sequences from sequencing reads"
LABEL about.url="https://github.com/marcelm/cutadapt"
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/marcelm/cutadapt/blob/main/LICENSE"
LABEL about.publication="http://dx.doi.org/10.14806/ej.17.1.200"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
# COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

RUN conda install -y -c conda-forge -c anaconda mamba
# Install additional R packages from conda-forge using conda (this tag doesn't contain mamba)
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# Install additional Python packages
# RUN pip install -r /tmp/python-packages.txt

USER $NB_UID
