################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="PRIESSTESS"
LABEL software.version="4de5ced180f3dabcbcd802e0f150f41c5c7d37b2"
LABEL about.summary="Predictive RBP-RNA InterpretablE Sequence-Structure moTif regrESSion"
LABEL about.url="https://github.com/kaitlin309/PRIESSTESS"
LABEL about.license=""
LABEL about.license_file=""
LABEL about.publication="https://doi.org/10.1093/nar/gkac694"
LABEL about.tags="Genomics"

USER root

ENV conda_env=PRIESSTESS

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN conda create -c bioconda -c conda-forge -c anaconda -n ${conda_env} python=3.8 mamba 

SHELL ["conda","run","-n","PRIESSTESS","/bin/bash","-c"]

RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN cd /opt && \
  git clone https://github.com/kaitlin309/PRIESSTESS && \
  cd /opt/PRIESSTESS && \
  git checkout 4de5ced180f3dabcbcd802e0f150f41c5c7d37b2

# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/${conda_env}/bin/python" -m ipykernel install --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    fix-permissions "/opt/PRIESSTESS"

RUN chmod +x /opt/PRIESSTESS/PRIESSTESS
RUN chmod +x /opt/PRIESSTESS/PRIESSTESS_scan
RUN chmod +x /opt/PRIESSTESS/bin/utils/*
RUN chmod +x /opt/PRIESSTESS/bin/*

USER $NB_UID

ENV PATH /opt/PRIESSTESS/:$PATH
ENV PATH /opt/conda/envs/${conda_env}/bin/:$PATH

#RUN echo $conda_env
#RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"


