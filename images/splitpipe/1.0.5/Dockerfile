################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="splitpipe"
LABEL software.version="1.0.5"
LABEL about.summary="splitpipe software for processing parse bio scRNA data."
LABEL about.url="parsebiosciences.com"
LABEL about.license_file="https://support.parsebiosciences.com/hc/en-us/article_attachments/13629631420308/Parse_Biosciences_Software_License_Agreement.pdf"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY ParseBiosciences-Pipeline.1.0.5p /opt/ParseBiosciences-Pipeline.1.0.5p

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN cd /opt/ParseBiosciences-Pipeline.1.0.5p && \
  bash ./install_TCR.sh -i -y && \
  pip install --no-cache-dir ./ && \
  bash ./install_TCR.sh -c

RUN cd && \
  mkdir analysis expdata genomes;

USER $NB_UID
