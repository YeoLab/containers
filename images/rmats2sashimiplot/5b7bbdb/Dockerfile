################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="rmats2sashimiplot"
LABEL software.version="5b7bbdb"
LABEL about.summary="rmats2sashimiplot produces a sashimiplot visualization of rMATS output"
LABEL about.url="https://github.com/Xinglab/rmats2sashimiplot"
LABEL about.license="GPL-2"
LABEL about.license_file="https://github.com/Xinglab/rmats2sashimiplot?tab=readme-ov-file#GPL-2.0-1-ov-file"
LABEL about.publication=""
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

RUN cd /opt && \
    git clone https://github.com/Xinglab/rmats2sashimiplot && \
    cd /opt/rmats2sashimiplot && \
    sh 2to3.sh && \
    python setup.py install

USER $NB_UID
