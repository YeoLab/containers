
################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="R"
LABEL software.version="3.2.4"
LABEL about.summary="Reference-guided transcript discovery and quantification for long read RNA-Seq data"
LABEL about.home="https://github.com/GoekeLab/bambu"
LABEL about.documentation="https://bioconductor.org/packages/release/bioc/vignettes/bambu/inst/doc/bambu.html"
LABEL about.license_file="https://github.com/GoekeLab/bambu/blob/devel/LICENSE"
LABEL about.license="GPL-3"
LABEL about.citation_file="https://github.com/GoekeLab/bambu/blob/devel/inst/CITATION"
LABEL about.tags="Genomics"
  
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

COPY conda-packages-R.txt /tmp/conda-packages-R.txt
COPY test.R /tmp/test.R

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages-R.txt

RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github(repo = "GoekeLab/bambu", ref = "v3.2.4")'
RUN Rscript -e 'IRkernel::installspec(name = "r_bambu", displayname = "R bambu", user = FALSE)'

RUN Rscript /tmp/test.R

USER $NB_UID
