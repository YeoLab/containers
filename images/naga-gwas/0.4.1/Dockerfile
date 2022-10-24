################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook"
LABEL version="1"
LABEL software="naga-gwas"
LABEL software.version="0.4.1"
LABEL about.summary="Network Assisted Genomic Analysis Package"
LABEL about.publication=""
LABEL about.tags="Genomics"
LABEL about.web="https://github.com/shfong/naga/"
LABEL about.license_file="https://github.com/shfong/naga/blob/master/LICENSE"
LABEL about.license="MIT"

ENV PYTHON_VERSION=3.7
USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY python-packages.txt /tmp/python-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

RUN conda create -n 'nagagwas-0.4.1' -c conda-forge python=${PYTHON_VERSION} mamba

SHELL ["conda", "run", "-n", "nagagwas-0.4.1", "/bin/bash", "-c"]

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

# Install additional packages from conda-forge using mamba
RUN mamba install -y -c conda-forge --file /tmp/conda-packages.txt
RUN mamba install -y -c conda-forge ipykernel
RUN python -m ipykernel install --name nagagwas-0.4.1 --display-name "Python3 (nbgwas-0.4.1)"

USER $NB_UID

ENV PATH /opt/conda/envs/nagagwas-0.4.1/bin:$PATH

