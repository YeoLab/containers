FROM jupyter/datascience-notebook:hub-2.2.2

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
    perl

RUN conda init bash && \
    . ~/.bashrc && \
    conda install -y -c bioconda fastqc=0.12.1

USER $NB_UID
