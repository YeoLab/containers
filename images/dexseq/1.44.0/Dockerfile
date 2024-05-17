################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="dexseq"
LABEL software.version="1.48.0"
LABEL about.summary="Inference of differential exon usage in RNA-Seq"
LABEL about.url="https://bioconductor.org/packages/3.18/bioc/html/DEXSeq.html"
LABEL about.license="LGPL (>= 3)"
LABEL about.publication="https://doi.org/10.1073/pnas.1307202110"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install(c("GenomeInfoDbData", "GenomicAlignments", "GenomicFeatures", "DEXSeq", "Rsamtools"))'
RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN cd /opt && wget https://cran.r-project.org/src/contrib/curl_5.2.1.tar.gz
RUN R CMD INSTALL --configure-vars='INCLUDE_DIR=/opt/conda/include/ LIB_DIR=/opt/conda/lib/' /opt/curl_5.2.1.tar.gz
# RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install("UCSC.utils")'  # not available
RUN Rscript -e 'devtools::install_github("Bioconductor/UCSC.utils", ref = "e7cd20fd138bb949853e1810b1d85d94ebefc121")'
RUN Rscript -e 'devtools::install_github("Bioconductor/txdbmaker", ref = "dcc6dfc92edf577733cd540069f04d41292cd7c1")'

USER $NB_UID
