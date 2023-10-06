FROM jupyter/minimal-notebook:python-3.11

USER root

ENV DEBIAN_FRONTEND=non-interactive

RUN apt-get update && apt-get install -y \
    wget \
    less \
    curl \
    unzip \
    gcc \
    g++ \
    make \
    zlib1g-dev \
    libncurses5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-gnutls-dev \
    libssl-dev \
    perl \
    libsigsegv-dev

RUN conda init bash && \
    . ~/.bashrc && \
    conda install -y -c bioconda bedtools=2.31.0

RUN apt-get install -y gzip

USER $NB_UID
