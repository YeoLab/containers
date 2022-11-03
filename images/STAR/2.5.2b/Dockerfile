################## BASE IMAGE ######################

FROM centos:centos7

################## METADATA ######################

LABEL base_image="centos:centos7"
LABEL version="1"
LABEL software="STAR"
LABEL software.version="2.5.2b"
LABEL about.summary="Spliced Transcripts Alignment to a Reference"
LABEL about.home="https://github.com/alexdobin/STAR"
LABEL about.documentation="https://github.com/alexdobin/STAR/blob/master/doc/STARmanual.pdf"
LABEL about.license_file="https://github.com/alexdobin/STAR/blob/master/LICENSE"
LABEL about.license=""
LABEL about.tags="Genomics"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

RUN yum update -y && yum install -y wget
RUN cd /opt/ && wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN cd /opt && bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda/
ENV PATH /opt/conda/bin:$PATH
RUN conda update conda;
RUN conda install -y -c bioconda star=2.5.2b
CMD ["STAR"]
