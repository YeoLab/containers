################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="samtools"
LABEL software.version="1.17"
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

RUN yum update -y && yum install -y wget
RUN cd /opt/ && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN cd /opt && bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda/
ENV PATH /opt/conda/bin:$PATH
RUN conda update conda;
RUN conda install "samtools>=1.17"
CMD ["samtools"]
USER $NB_UID