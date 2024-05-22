################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software=""
LABEL software.version="4.0.0"
LABEL about.summary="Scalable De Novo Isoform Discovery from PacBio HiFi Reads + (pacbio packages and utilities)"
LABEL about.home="https://isoseq.how/"
LABEL about.documentation=""
LABEL about.license_file="https://github.com/PacificBiosciences/pbbioconda?tab=BSD-3-Clause-Clear-1-ov-file#readme"
LABEL about.license="BSD-3-Clause-Clear license"
LABEL about.tags="Genomics"
  
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
ARG conda_env=pacbio

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

COPY conda-packages.txt /tmp/conda-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba create -y -n ${conda_env} python=3.7
RUN mamba install -p "${CONDA_DIR}/envs/${conda_env}" -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/${conda_env}/bin/python" -m ipykernel install --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
    
USER $NB_UID
ENV PATH /opt/conda/envs/${conda_env}/bin/:$PATH
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"

USER $NB_UID
