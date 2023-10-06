FROM jupyter/minimal-notebook:python-3.11

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
    perl \
    libpcre2-dev \
    libpcre3-dev

RUN conda init bash && \
    . ~/.bashrc && \
    conda install -y -c bioconda pcre star=2.7.10b

USER $NB_UID
ENV LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu/:$LD_LIBRARY_PATH
