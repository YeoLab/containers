################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="R"
LABEL software.version="1.0.0"
LABEL about.summary="Contains essential software packages for analyzing proteomics-type data"
LABEL about.home="artms.org"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license="GPL-3"
LABEL about.tags="Proteomics"

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

RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install(c("artMS"))'
RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github(repo = "dnusinow/cRomppass", ref = "de872c086a5bb19d5ac46c4a451ef51172cef190")'

USER $NB_UID

