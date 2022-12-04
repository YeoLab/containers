################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="pacbio_pipeline"
LABEL software.version="v2"
LABEL about.summary="Collection of packages for processing bulk and single-cell Iso-Seq data"
LABEL about.url="https://isoseq.how/getting-started.html"
LABEL about.license=""
LABEL about.license_file="https://github.com/PacificBiosciences/IsoSeq/blob/master/LICENSE"
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

# COPY apt-packages.txt /tmp/apt-packages.txt
COPY pacbio_pipeline2.yml /tmp/pacbio_pipeline2.yml

# Update image, install additional distro packages
# RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN conda env create -f /tmp/pacbio_pipeline2.yml

SHELL ["conda","run","-n","pacbio_pipeline2","/bin/bash","-c"]

USER $NB_UID

ENV PATH /opt/conda/envs/pacbio_pipeline2/bin/:$PATH
