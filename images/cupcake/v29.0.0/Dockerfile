################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="cDNA_Cupcake"
LABEL software.version="v29.0.0"
LABEL about.summary="Miscellaneous collection of Python and R scripts for processing Iso-Seq data"
LABEL about.url="https://github.com/Magdoll/cDNA_Cupcake"
LABEL about.license="BSD-3-Clause-Clear license"
LABEL about.license_file="https://github.com/Magdoll/cDNA_Cupcake/blob/master/LICENSE.md"
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

# COPY apt-packages.txt /tmp/apt-packages.txt
COPY Cupcake_SQANTI3.yml /tmp/Cupcake_SQANTI3.yml

# Update image, install additional distro packages
# RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN conda env create -f /tmp/Cupcake_SQANTI3.yml

SHELL ["conda","run","-n","SQANTI3.env","/bin/bash","-c"]

RUN echo which python && \
  cd /opt && \
  wget https://github.com/Magdoll/cDNA_Cupcake/archive/refs/tags/v29.0.0.tar.gz && \
  tar -xvf /opt/v29.0.0.tar.gz && \
  cd /opt/cDNA_Cupcake-29.0.0/ && \
  python setup.py build && \
  python setup.py install

SHELL ["conda","run","-n","SQANTI3.env","/bin/bash","-c"]

USER $NB_UID

ENV PATH /opt/conda/envs/SQANTI3.env/bin/:$PATH
# ENV PYTHONPATH /opt/cDNA_Cupcake-29.0.0/sequence:$PYTHONPATH

