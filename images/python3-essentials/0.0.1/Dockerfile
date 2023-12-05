################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software=""
LABEL software.version="0.0.1"
LABEL about.summary="Contains essential bioinformatics python3 packages, plus other software essential for bioinformatics analysis."
LABEL about.home="https://hub.docker.com/repository/docker/brianyee/python3-essentials"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Bioinformatics"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY environment.yaml /tmp/environment.yaml

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# you can add additional libraries you want mamba to install by listing them below the first line and ending with "&& \"
RUN mamba env update --file /tmp/environment.yaml -p "${CONDA_DIR}/envs/python3essential-0.0.1" && \
    mamba clean --all -f -y

ARG conda_env=python3essential-0.0.1
# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/${conda_env}/bin/python" -m ipykernel install --name="python3essential-0.0.1" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID
ENV PATH /opt/conda/envs/python3essential-0.0.1/bin/:$PATH
RUN echo "conda activate python3essential-0.0.1" >> "${HOME}/.bashrc"

