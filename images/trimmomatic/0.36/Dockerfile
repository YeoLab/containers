################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="trimmomatic"
LABEL software.version="0.36"
LABEL about.summary="A flexible read trimming tool for Illumina NGS data. Performs adapter clipping, quality trimming and length filtering on paired-end or single-end reads."
LABEL about.home="https://github.com/yeolab/containers"
LABEL about.url="http://www.usadellab.org/cms/?page=trimmomatic"
LABEL about.documentation="http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/TrimmomaticManual_V0.32.pdf"
LABEL about.license="GPL-3.0"
LABEL about.license_file="https://github.com/usadellab/Trimmomatic/blob/main/LICENSE"
LABEL about.publication="https://doi.org/10.1093/bioinformatics/btu170"
LABEL about.tags="Genomics"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install trimmomatic (pulls openjdk) from bioconda using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# The bundled adapter FASTAs live under a build-suffixed share/ directory
# (e.g. share/trimmomatic-0.36-6/adapters). Expose them at a stable path so
# ILLUMINACLIP arguments do not have to encode the conda build number.
RUN ln -s "$(dirname "$(ls -d /opt/conda/share/trimmomatic-0.36*/adapters | head -1)")/adapters" \
        /opt/trimmomatic-adapters

ENV TRIMMOMATIC_ADAPTERS /opt/trimmomatic-adapters

RUN trimmomatic -version && ls /opt/trimmomatic-adapters

USER $NB_UID
