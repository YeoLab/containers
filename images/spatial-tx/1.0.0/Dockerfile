################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="R, Python3"
LABEL software.version="1.0.0"
LABEL about.summary="Container with some spatial transcriptomics + single cell software installed"
LABEL about.home="https://github.com/yeolab/containers"
LABEL about.documentation=""
LABEL about.RCTD.publication="https://www.nature.com/articles/s41587-021-00830-w"
LABEL about.RCTD.license_file="https://github.com/dmcable/spacexr/blob/master/LICENSE"
LABEL about.RCTD.license="GNU"
LABEL about.SPOTlight.publication="doi:10.1093/nar/gkab043"
LABEL about.SPOTlight.license_file="https://github.com/BioTuring-Notebooks/SPOTlight/blob/main/LICENSE.md"
LABEL about.SPOTlight.license="GPL-3"
LABEL about.Tangram.publication=""
LABEL about.Tangram.license_file=""
LABEL about.Tangram.license=""
LABEL about.tags=""

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>


USER root

RUN apt-get update

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c r -c conda-forge -c anaconda --file /tmp/conda-packages.txt

RUN pip install -r /tmp/python-packages.txt
RUN pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install git+https://github.com/BayraktarLab/cell2location.git#egg=cell2location[tutorials]

RUN Rscript -e 'devtools::install_github("https://github.com/MarcElosua/SPOTlight", ref = "87534b92311aec0f254297dcb9478e4b63e9ee81")'
RUN Rscript -e 'devtools::install_github("xzhoulab/SPARK")'
RUN Rscript -e 'devtools::install_github("satijalab/seurat-data")'

COPY dmcable-spacexr-ead0e5b.tar.gz /opt/dmcable-spacexr-ead0e5b.tar.gz
RUN cd /opt && \
  tar -xvf dmcable-spacexr-ead0e5b.tar.gz && \
  Rscript -e 'devtools::install("/opt/dmcable-spacexr-ead0e5b", build_vignettes = FALSE)' && \
  rm dmcable-spacexr-ead0e5b.tar.gz && \
  rm -rf /opt/dmcable-spacexr-ead0e5b

ENV NUMBA_CACHE_DIR=/home/jovyan

USER $NB_UID

