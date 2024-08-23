################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="eugene"
LABEL software.version="0.1.2"
LABEL about.summary="Elucidating the Utility of Genomic Elements with Neural Nets"
LABEL about.url="https://eugene-tools.readthedocs.io/"
LABEL about.license="MIT"
LABEL about.publication="https://eugene-tools.readthedocs.io/en/latest/references.html"
LABEL about.license_file="https://github.com/ML4GLand/EUGENe/tree/main?tab=MIT-1-ov-file#readme"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt
# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt --ignore-installed

USER $NB_UID
