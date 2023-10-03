FROM jupyter/minimal-notebook:python-3.11

USER root
ENV DEBIAN_FRONTEND=non-interactive

RUN sudo apt-get update && sudo apt-get install -y \
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

RUN mamba install -y -c bioconda fastqc=0.12.1

USER $NB_USER
