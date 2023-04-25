################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="2"
LABEL software="seurat"
LABEL software.version="4.3.0"
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
RUN Rscript -e 'devtools::install_github("mojaveazure/seurat-disk")'
RUN Rscript -e 'devtools::install_github("satijalab/seurat-data")'

RUN Rscript -e 'devtools::install_github(repo = "vertesy/Stringendo", upgrade = F)'
RUN Rscript -e 'devtools::install_github(repo = "vertesy/CodeAndRoll2", upgrade = F)'
RUN Rscript -e 'devtools::install_github(repo = "vertesy/ReadWriter", upgrade = F)'
RUN Rscript -e 'devtools::install_github(repo = "vertesy/MarkdownHelpers", upgrade = F)'
RUN Rscript -e 'devtools::install_github(repo = "vertesy/MarkdownReports", upgrade = F)'
RUN Rscript -e 'devtools::install_github(repo = "vertesy/ggExpress", upgrade = F)'
RUN Rscript -e 'devtools::install_github(repo = "vertesy/DatabaseLinke.R", upgrade = F)'
RUN Rscript -e 'devtools::install_github(repo = "vertesy/Seurat.utils", upgrade = F, ref = "v1.5.2")'
RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org"); BiocManager::install(c("GenomeInfoDbData", "org.Hs.eg.db"))'

RUN Rscript -e 'devtools::install_github(repo = "jn-goe/gruffi", upgrade = F)'

USER $NB_UID
