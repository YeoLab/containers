################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:r-4.1.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:r-4.1.2"
LABEL version="1"
LABEL software="R"
LABEL software.version="b3e7a0b"
LABEL about.summary="NicheNet: predict active ligand-target links between interacting cells"
LABEL about.home="https://github.com/saeyslab/nichenetr/"
LABEL about.documentation=""
LABEL about.publication="doi:10.1038/s41592-019-0667-5"
LABEL about.publication="doi:10.1016/j.immuni.2019.08.017"
LABEL about.publication="doi:10.1016/j.cell.2021.12.018"
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags=""

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

RUN apt-get update

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge --file /tmp/conda-packages.txt

RUN Rscript -e 'devtools::install_github("saeyslab/nichenetr@b3e7a0b20dc7e09455b702807d55e9adef4e4787")'
RUN Rscript -e 'IRkernel::installspec(name = "nichenetr-b3e7a0b", displayname = "NicheNetR-b3e7a0b", user = FALSE)'
USER $NB_UID

