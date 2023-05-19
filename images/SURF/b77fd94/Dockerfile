################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="R"
LABEL software.version="b77fd94"
LABEL about.summary="The statistical utility for RBP functions (SURF)"
LABEL about.home="https://github.com/keleslab/surf"
LABEL about.documentation=""
LABEL about.license_file="https://github.com/keleslab/surf/blob/master/LICENSE.md"
LABEL about.license="GPL-3"
LABEL about.tags="Genomics"
  
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

COPY conda-packages-R.txt /tmp/conda-packages-R.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages-R.txt

RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github(repo = "keleslab/surf", ref = "b77fd948b76d974752bd61b260c7faf33e110182")'

USER $NB_UID
