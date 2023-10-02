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
    zlib1g \
    libncurses5-dev \
    libncursesw5-dev \
    libbz2-dev \
    liblzma-dev \
    libcurl4-openssl-dev

RUN cd /opt && \
  wget https://github.com/samtools/samtools/releases/download/1.17/samtools-1.17.tar.bz2 && \
  tar -xjf /opt/samtools-1.17.tar.bz2 && \
  cd /opt/samtools-1.17 && \
  ./configure --prefix=/opt/samtools-1.17-build && \
  make && \
  make install && \
  rm -rf /opt/samtools-1.17 && \
  rm /opt/samtools-1.17.tar.bz2
RUN cd /opt && \
  wget https://github.com/samtools/bcftools/releases/download/1.17/bcftools-1.17.tar.bz2 && \
  tar -xjf /opt/bcftools-1.17.tar.bz2 && \
  cd /opt/bcftools-1.17 && \
  ./configure --prefix=/opt/bcftools-1.17-build && \
  make && \
  make install && \
  rm -rf /opt/bcftools-1.17 && \
  rm /opt/bcftools-1.17.tar.bz2

ENV PATH /opt/samtools-1.17-build/bin:/opt/bcftools-1.17-build/bin:$PATH

USER $NB_UID