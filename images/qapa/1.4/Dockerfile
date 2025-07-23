################## BASE IMAGE ######################

FROM jupyter/scipy-notebook:latest

################## METADATA ######################

LABEL base_image="jupyter/scipy-notebook:latest"
LABEL version="1"
LABEL software="QAPA"
LABEL software.version="1.4"
LABEL about.summary="RNA-seq Quantification of Alternative Polyadenylation"
LABEL about.url="https://github.com/morrislab/qapa"
LABEL about.license="GPL3"
LABEL about.license_file="https://github.com/morrislab/qapa?tab=GPL-3.0-1-ov-file#readme"
LABEL about.publication="https://genomebiology.biomedcentral.com/articles/10.1186/s13059-018-1414-4"
LABEL about.tags="Genomics"

USER root

ARG conda_env=qapa

# Update image, install additional distro packages
RUN apt-get update

# you can add additional libraries you want mamba to install by listing them below the first line and ending with "&& \"
RUN cd /tmp && \
    git clone https://github.com/morrislab/qapa

COPY environment.yml /tmp/qapa/environment.yml

RUN mamba env update --file /tmp/qapa/environment.yml -p "${CONDA_DIR}/envs/${conda_env}" && \
    mamba clean --all -f -y

RUN fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID
ENV PATH /opt/conda/envs/${conda_env}/bin/:$PATH
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"


