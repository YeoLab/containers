################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="moccasin"
LABEL software.version="0.25"
LABEL about.summary="This is a script for splicing confounding factor adjustment for use with MAJIQ 2.1."
LABEL about.url="https://bitbucket.org/biociphers/moccasin/"
LABEL about.license="MIT"
LABEL about.license_file=""
LABEL about.publication="https://doi.org/10.1093/bioinformatics/btx790"
LABEL about.publication="https://doi.org/10.1038/nbt.2931"
LABEL about.publication="https://doi.org/10.7554/eLife.11752.001"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

RUN conda create -c anaconda -n "moccasin" python=3.8.6

SHELL ["conda", "run", "-n", "moccasin", "/bin/bash", "-c"]

RUN cd /opt && \
    git clone https://bitbucket.org/biociphers/moccasin.git && \
    cd /opt/moccasin && \
    pip install -r requirements.txt

RUN sed -i '1i#!/usr/bin/env python' /opt/moccasin/moccasin.py && \
    chmod +x /opt/moccasin/moccasin.py

ENV PATH=/opt/conda/envs/moccasin/bin:/opt/moccasin:$PATH

USER $NB_UID
