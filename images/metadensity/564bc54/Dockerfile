################## BASE IMAGE ######################

FROM jupyter/scipy-notebook:latest

################## METADATA ######################

LABEL base_image="jupyter/scipy-notebook:latest"
LABEL version="1"
LABEL software="metadensity"
LABEL software.version="0.0.1 (commit: 6259055)"
LABEL about.summary="Define metadensity to predict RNA binding protein function"
LABEL about.url="https://github.com/algaebrown/metadensity"
LABEL about.license=""
LABEL about.license_file=""
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY environment.yaml /tmp/environment.yaml
COPY conda-packages.txt /tmp/conda-packages.txt

ARG conda_env=metadensity

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# you can add additional libraries you want mamba to install by listing them below the first line and ending with "&& \"
RUN mamba env update --file /tmp/environment.yaml -p "${CONDA_DIR}/envs/${conda_env}" && \
    mamba clean --all -f -y
    
RUN cd /opt && git clone https://github.com/algaebrown/Metadensity.git
WORKDIR /opt/Metadensity
RUN git pull
COPY config.py /opt/Metadensity/metadensity/config.py
RUN /opt/conda/envs/${conda_env}/bin/pip install -e .

# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/${conda_env}/bin/python" -m ipykernel install --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# Install additional R packages from conda-forge using mamba
RUN mamba install -p "${CONDA_DIR}/envs/${conda_env}" -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt
    
USER $NB_UID
ENV PATH /opt/conda/envs/${conda_env}/bin/:$PATH
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"


