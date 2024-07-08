################## BASE IMAGE ######################

FROM jupyter/scipy-notebook:latest

################## METADATA ######################

LABEL base_image="jupyter/scipy-notebook:latest"
LABEL version="1"
LABEL software="DESeq2"
LABEL software.version="1.40"
LABEL about.summary="DESeq2 is a software package written for the analysis of high-throughput RNA sequencing data to identify differentially expressed genes between different experimental conditions"
LABEL about.url="https://github.com/thelovelab/DESeq2"
LABEL about.license="LGPL"
LABEL about.license_file=""
LABEL about.publication="https://genomebiology.biomedcentral.com/articles/10.1186/s13059-014-0550-8"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY environment.yaml /tmp/environment.yaml

ARG conda_env=deseq2

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# you can add additional libraries you want mamba to install by listing them below the first line and ending with "&& \"
RUN mamba env update --file /tmp/environment.yaml -p "${CONDA_DIR}/envs/${conda_env}" && \
    mamba clean --all -f -y

# RUN /opt/conda/envs/${conda_env}/bin/Rscript -e 'install.packages("argparse", repos = "https://cran.us.r-project.org")'
RUN /opt/conda/envs/${conda_env}/bin/Rscript -e 'IRkernel::installspec(name = "deseq2_1.39.3", displayname = "DESeq2-1.40", user = FALSE)' && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

USER $NB_UID
ENV PATH /opt/conda/envs/${conda_env}/bin/:$PATH
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"


