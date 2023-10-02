FROM jupyter/datascience-notebook:hub-2.2.2

USER root

ENV DEBIAN_FRONTEND=non-interactive

RUN apt-get update && apt-get install -y \
    wget \
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
    conda install -y -c bioconda star=2.7.10b

USER $NB_UID