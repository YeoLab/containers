################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:python-3.7.12

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:python-3.10.11"
LABEL version="1"
LABEL software="SNAF"
LABEL software.version="e23ce39"
LABEL about.summary="Splicing Neo Antigen Finder (SNAF) is an easy-to-use Python package to identify splicing-derived tumor neoantigens from RNA sequencing data, it further leverages both deep learning and hierarchical Bayesian models to prioritize certain candidates for experimental validation"
LABEL about.home="https://github.com/frankligy/SNAF"
LABEL about.documentation="https://snaf.readthedocs.io/"
LABEL about.tags=""
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/frankligy/SNAF#MIT-1-ov-file"
LABEL about.publication="https://www.science.org/doi/10.1126/scitranslmed.ade2886"
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
#COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
#RUN mamba install -y -c bioconda -c r -c conda-forge -c anaconda --file /tmp/conda-packages.txt
RUN pip install --ignore-installed llvmlite
RUN pip install --ignore-installed git+https://github.com/frankligy/SNAF.git@e23ce39512a1a7f58c74e59b4b7cedc89248b908
RUN pip install seaborn==0.11.2
USER $NB_UID
