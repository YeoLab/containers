################## BASE IMAGE ######################

FROM jupyter/r-notebook

################## METADATA ######################

LABEL base_image="jupyter/r-notebook"
LABEL version="1"
LABEL software="R"
LABEL software.version="1.10.2"
LABEL about.summary="artMS provides a set of tools for the analysis of proteomics label-free datasets. "
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
RUN mamba install -y -c bioconda -c r -c conda-forge --file /tmp/conda-packages.txt # Required by umap-learn

RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install(c("artMS"))'
RUN Rscript -e 'IRkernel::installspec(name = "artms-1.10.2", displayname = "artMS-1.10.2", user = FALSE)'

USER $NB_UID

