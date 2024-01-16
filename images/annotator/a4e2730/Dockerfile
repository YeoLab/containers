################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="annotator"
LABEL software.version="a4e2730"
LABEL about.summary="Annotates bed files"
LABEL about.url="https://github.com/byee4/annotator"
LABEL about.license="UCSD"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN cd /opt && \
	git clone https://github.com/byee4/annotator && \
	cd annotator && \
        pip install -e .

USER $NB_UID
