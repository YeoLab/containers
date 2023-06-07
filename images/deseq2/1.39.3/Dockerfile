################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="deseq2"
LABEL software.version="1.39.3"
LABEL about.summary="Differential gene expression analysis based on the negative binomial distribution"
LABEL about.url="https://bioconductor.org/packages/3.16/bioc/html/DESeq2.html"
LABEL about.license="LGPL (>= 3)"
LABEL about.publication="10.1186/s13059-014-0550-8"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN Rscript -e 'install.packages("devtools", repos = "https://cran.us.r-project.org")'
# RUN Rscript -e 'install.packages("RCurl", repos = "https://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github("mikelove/deseq2", ref = "98d2ab74df97e2e97943fa5c996d292ef2aba180")'

#USER $NB_UID
