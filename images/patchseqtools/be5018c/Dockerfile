################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="0.1"
LABEL software="patchseqtools"
LABEL software.version="be5018ccd2e1a6caea7bc7628a203f6214915bcf"
LABEL about.summary="QC and cell type assignment for patch-seq transcriptomics data."
LABEL about.publication="https://elifesciences.org/articles/65482"
LABEL about.license="BSD-2"
LABEL about.license_file="https://github.com/AllenInstitute/patchseqtools/blob/master/LICENSE"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY python-packages.txt /tmp/python-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c conda-forge --file /tmp/conda-packages.txt # Required by umap-learn

# Install additional R packages via Rscript
RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github(repo = "PavlidisLab/patchSeqQC", ref = "8b8b4022243f26106f0190c52d419a0029fdc88b")'
RUN Rscript -e 'devtools::install_github(repo = "AllenInstitute/patchseqtools", ref = "be5018ccd2e1a6caea7bc7628a203f6214915bcf")'
RUN Rscript -e 'IRkernel::installspec(name = "patchseqtools-be5018c", displayname = "R (patchseqtools-be5018c)", user = FALSE)'

USER $NB_UID
