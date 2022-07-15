################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="pureclip"
LABEL software.version="1.3.1"
LABEL about.summary="Capturing protein-RNA interaction footprints from single-nucleotide CLIP-seq data"
LABEL about.url="https://github.com/skrakau/PureCLIP"
LABEL about.license="GPL-3.0"
LABEL about.license_file="https://github.com/skrakau/PureCLIP/blob/master/LICENSE.md"
LABEL about.publication="https://doi.org/10.1186/s13059-017-1364-2"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
# COPY conda-packages.txt /tmp/conda-packages.txt
# COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
# RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# Install additional Python packages
# RUN pip install -r /tmp/python-packages.txt

RUN cd /opt && \
  git clone https://github.com/skrakau/PureCLIP && \
  mkdir /opt/PureCLIP/build && \
  cd /opt/PureCLIP/build && \
  cmake ../src && \
  make

ENV PATH=/opt/PureCLIP/build/:$PATH

USER $NB_UID
