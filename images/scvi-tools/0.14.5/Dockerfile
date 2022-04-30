################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook::hub-2.0.2"
LABEL version="2"
LABEL software="scvi-tools"
LABEL software.version="0.14.5"
LABEL about.summary="scvi-tools accelerates data analysis and model development, powered by PyTorch and AnnData."
LABEL about.url="https://scvi-tools.org/"
LABEL about.license="BSD-3"
LABEL about.license_file="https://github.com/scverse/scvi-tools/blob/master/LICENSE"
LABEL about.publication="https://doi.org/10.1038/s41587-021-01206-w"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge -c anaconda --file /tmp/conda-packages.txt

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

# RUN /opt/conda/bin/python -m ipykernel install --user --display-name="scvi-tools-0.14.5" --name="scvi-tools-0.14.5" && \
#     fix-permissions "/opt/conda/" && \
#     fix-permissions "/home/${NB_USER}"
ENV NUMBA_CACHE_DIR "/home/${NB_USER}"    
USER $NB_UID
