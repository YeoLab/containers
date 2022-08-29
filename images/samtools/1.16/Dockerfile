################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="samtools"
LABEL software.version="1.16"
LABEL about.summary=""
LABEL about.url="https://www.htslib.org/download/"
LABEL about.license=""
LABEL about.license_file=""
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

RUN cd /opt && \
  wget https://github.com/samtools/samtools/releases/download/1.16/samtools-1.16.tar.bz2 && \
  tar -xjf /opt/samtools-1.16.tar.bz2 && \
  cd /opt/samtools-1.16 && \
  ./configure --prefix=/opt/samtools-1.16-build && \
  make && \
  make install && \
  rm -rf /opt/samtools-1.16 && \
  rm /opt/samtools-1.16.tar.bz2

RUN cd /opt && \
  wget https://github.com/samtools/bcftools/releases/download/1.16/bcftools-1.16.tar.bz2 && \
  tar -xjf /opt/bcftools-1.16.tar.bz2 && \
  cd /opt/bcftools-1.16 && \
  ./configure --prefix=/opt/bcftools-1.16-build && \
  make && \
  make install && \
  rm -rf /opt/bcftools-1.16 && \
  rm /opt/bcftools-1.16.tar.bz2

ENV PATH /opt/samtools-1.16-build/bin:/opt/bcftools-1.16-build/bin:$PATH
USER $NB_UID
