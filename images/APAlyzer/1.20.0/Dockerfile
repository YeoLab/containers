################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="APAlyzer"
LABEL software.version="1.20.0"
LABEL about.summary="A toolkit for APA analysis using RNA-seq data"
LABEL about.url="https://bioconductor.org/packages/3.20/bioc/html/APAlyzer.html"
LABEL about.license="LGPL-3"
LABEL about.license_file=""
LABEL about.publication="https://doi.org/10.1093/bioinformatics/btaa266"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Set R to use single architecture
ENV R_ARCH=""
RUN echo 'options(install.packages.compile.from.source = "never")' >> /opt/conda/lib/R/etc/Rprofile.site

# Genomic features/GenomeInfoDb never seems to work through conda...
RUN Rscript -e 'install.packages("pkgbuild", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'install.packages("callr", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install("GenomeInfoDb", force = TRUE)'
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install("GenomeInfoDbData", force = TRUE)'
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install(c("org.Hs.eg.db", "org.Hs.eg.db"), force = TRUE)'
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org");BiocManager::install(c("ggplot2", "repmis", "Rsamtools", "APAlyzer"), force = TRUE)'
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

RUN Rscript -e 'IRkernel::installspec(name = "apalyzer-1.20.0", displayname = "APAlyzer 1.20.0", user = FALSE)'
USER $NB_UID
