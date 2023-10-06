FROM jupyter/minimal-notebook:python-3.11

USER root

ENV DEBIAN_FRONTEND=non-interactive

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    zip \
    unzip \
    gcc \
    g++ \
    make \
    tar \
    gzip \
    perl

RUN mkdir /homer && cd /homer \
    && curl http://homer.ucsd.edu/homer/configureHomer.pl -o configureHomer.pl \
    && perl configureHomer.pl -install

ENV PATH="/homer/bin/:$PATH"

RUN apt-get clean && rm -rf /var/lib/apt/lists/* && rm -rf *.tar.gz *.zip

USER $NB_UID
