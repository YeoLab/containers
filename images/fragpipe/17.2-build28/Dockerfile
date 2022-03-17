################## BASE IMAGE ######################

FROM prvst/philosopher:4.1.1

################## METADATA ######################

LABEL base_image="prvst/philosopher:4.1.1"
LABEL version="1"
LABEL software="fragpipe"
LABEL software.version="17.2-build28"
LABEL about.summary="A cross-platform Graphical User Interface (GUI) for running MSFragger and Philosopher - powered pipeline for comprehensive analysis of shotgun proteomics data"
LABEL about.url="https://github.com/Nesvilab/FragPipe"
LABEL about.license="GPL-3"
LABEL about.license_file="https://github.com/Nesvilab/FragPipe/blob/master/LICENSE"
LABEL about.publication="https://doi.org/10.1016/j.cell.2021.04.048"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install Mono 
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
  sh -c 'echo "deb https://download.mono-project.com/repo/ubuntu stable-xenial main" > /etc/apt/sources.list.d/mono-official-stable.list' && \
  apt-get update && \
  apt-get install -y mono-complete

RUN conda create -y -c bioconda -c conda-forge -n fragpipe python=3 \
  numpy \
  scipy \
  scikit-learn \
  statsmodels \
  pandas>=1.1.0 \
  biopython \
  pyopenms>=2.6.0 \
  matplotlib \
  seaborn

COPY FragPipe-17.2-build28.zip /opt/FragPipe-17.2-build28.zip
RUN cd /opt && unzip FragPipe-17.2-build28.zip

COPY MSFragger-3.4.zip /opt/MSFragger-3.4.zip
RUN cd /opt && unzip MSFragger-3.4.zip

ENV PATH /opt/fragpipe/bin:/opt/MSFragger-3.4/:/home/biodocker/bin/philosopher:/opt/conda/envs/fragpipe/bin/:$PATH
ENV JAVA_HOME /usr

RUN mkdir -p /usr/java && ln -s /usr /usr/java/latest

SHELL ["conda", "run", "-n", "fragpipe", "/bin/bash", "-c"]

# MSFragger.jar file: /opt/MSFragger-3.4/MSFragger-3.4.jar
# python directory: /opt/conda/envs/fragpipe/bin/
# Philosopher binary file: /home/biodocker/bin/philosopher