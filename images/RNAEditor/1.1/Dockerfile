################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="RNAEditor"
LABEL software.version="1.1a"
LABEL about.summary="RNAEditor is tool to analyze RNA editing events from RNA-seq data. It accepts Fastq and Bam files as input, handles all the analysis and filter steps for you and outputs comprehensive statistics and editing Islands."
LABEL about.url="https://github.com/djhn75/RNAEditor"
LABEL about.license=""
LABEL about.license_file=""
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

ENV conda_env=RNAEditor

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY picard-tools-1.119.zip /tmp/picard-tools-1.1119.zip

RUN cd /tmp && \
    unzip /tmp/picard-tools-1.1119.zip && \
    mv /tmp/picard-tools-1.119/* /usr/local/bin && \
    rm -rf /tmp/picard-tools-1.119/ && \
    rm /tmp/picard-tools-1.1119.zip

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# RUN add-apt-repository ppa:rock-core/qt4 && \
#     apt update && \
#     apt-get install -y libqt4-dev 

# Install additional packages from conda-forge using mamba
ENV PATH /opt/conda/bin:$PATH

RUN conda create -c bioconda -c conda-forge -c anaconda -n ${conda_env} python=3.8 mamba 

SHELL ["conda","run","-n","RNAEditor","/bin/bash","-c"]

RUN mamba install -y -c bioconda -c conda-forge -c anaconda --file /tmp/conda-packages.txt

RUN cd /opt && \
  wget https://github.com/djhn75/RNAEditor/archive/refs/tags/RNAEditor_v1.1_alpha.tar.gz && \
  tar -xvf /opt/RNAEditor_v1.1_alpha.tar.gz

COPY RNAEditor-RNAEditor_v1.1_alpha/RNAEditor.py /opt/RNAEditor-RNAEditor_v1.1_alpha/RNAEditor.py

ENV PATH /opt/conda/envs/RNAEditor/bin:/opt/RNAEditor-RNAEditor_v1.1_alpha/:$PATH

USER $NB_UID
