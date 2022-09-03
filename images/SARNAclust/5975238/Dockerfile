################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="SARNAclust"
LABEL software.version="5975238"
LABEL about.summary="RNApeakFold is an RNA secondary structure prediction tool tailored to CLIP peaks. SARNAclust is a clustering algorithm for CLIP peaks that typically uses the secondary structure prediction from RNAfold."
LABEL about.url="https://github.com/idotu/SARNAclust"
LABEL about.license="Apache-2.0"
LABEL about.license_file="https://github.com/idotu/SARNAclust/blob/master/LICENSE"
LABEL about.publication="https://doi.org/10.1371%2Fjournal.pcbi.1006078"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
#COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# Install additional Python packages
#RUN pip install -r /tmp/python-packages.txt
RUN pip install git+https://github.com/fabriziocosta/EDeN.git

USER $NB_UID
