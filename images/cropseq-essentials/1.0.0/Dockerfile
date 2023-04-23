################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.3.1

################## METADATA ######################

LABEL base_image="ubuntu:16.04"
LABEL version="1"
LABEL software="R, Python3"
LABEL software.version="1.0.0"
LABEL about.summary="1.0.0"
LABEL about.home="https://github.com/yeolab/containers"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Genomics"
  
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

COPY conda-packages-python.txt /tmp/conda-packages-python.txt
COPY conda-packages-R.txt /tmp/conda-packages-R.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c hailinwei -c bioconda -c conda-forge --file /tmp/conda-packages-python.txt
RUN mamba install -y -c hailinwei -c bioconda -c conda-forge --file /tmp/conda-packages-R.txt

RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github(repo = "katsevich-lab/sceptre", ref = "a3ef7b080675c195ca62928caa177783de91daf7")'
RUN Rscript -e 'devtools::install_github(repo = "HailinWei98/SCREE", ref = "a9bbfbb9c2a3ebfc03fe14cfc54415480b384233")'

# https://github.com/Microsoft/microsoft-r-open/issues/63
RUN Rscript -e 'remove.packages(c("curl","httr"))'
RUN Rscript -e 'IRkernel::installspec(name = "cropseq-essentials-1.0.0", displayname = "cropseq-essentials (1.0.0)", user = FALSE)'

RUN cd /opt && \
  git clone https://github.com/shendurelab/single-cell-ko-screens
# https://github.com/shendurelab/single-cell-ko-screens/issues/1
COPY get_barcodes.py /opt/single-cell-ko-screens/get_barcodes.py

COPY cellranger-7.1.0.tar.gz /opt/cellranger-7.1.0.tar.gz
RUN cd /opt && \
    tar --absolute-names -xzvf cellranger-7.1.0.tar.gz
ENV PATH=/opt/cellranger-7.1.0/:$PATH
CMD cellranger

COPY cellranger-atac-2.1.0.tar.gz /opt/cellranger-atac-2.1.0.tar.gz
RUN cd /opt && \
    tar --absolute-names -xzvf cellranger-atac-2.1.0.tar.gz
ENV PATH=/opt/cellranger-atac-2.1.0/:$PATH

USER $NB_UID

ENV PATH=/opt/single-cell-ko-screens:$PATH
