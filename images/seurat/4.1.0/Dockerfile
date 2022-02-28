################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:r-4.1.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:r-4.1.2"
LABEL version="1"
LABEL software="seurat"
LABEL software.version="4.1.0"
LABEL about.summary="R toolkit for single cell genomics"
LABEL about.url="www.satijalab.org/seurat"
LABEL about.license="MIT"
LABEL about.license_file="https://satijalab.org/seurat/license"
LABEL about.publication="https://doi.org/10.1016/j.cell.2021.04.048"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github(repo = "satijalab/seurat-data", ref = "b59556b24d7d6728a5744c9c715dd5f7f32ed7a5")'
RUN Rscript -e 'devtools::install_github(repo = "mojaveazure/seurat-disk", ref = "163f1aade5bac38ed1e9e9c912283a7e74781610")'

RUN Rscript -e 'IRkernel::installspec(name = "seurat-4.1.0", displayname = "seurat-4.1.0", user = FALSE)'
USER $NB_UID
