################## BASE IMAGE ######################

FROM debian:trixie

################## METADATA ######################

LABEL base_image="debian:trixie"
LABEL version="2"
LABEL software="rbp-maps"
LABEL software.version="v1.1.0"
LABEL about.summary="RNA-binding protein splicing and feature maps from CLIP-seq density or peaks"
LABEL about.url="https://github.com/YeoLab/rbp-maps"
LABEL about.license="MIT"
LABEL about.license_file=""
LABEL about.publication="https://www.ncbi.nlm.nih.gov/pubmed/30413564"
LABEL about.tags="Genomics,Transcriptomics,CLIP-seq,Splicing"

ARG RBP_MAPS_VERSION=v1.1.0

# Builds the tagged release with its own environment.yml (Python 3.13 plus
# samtools, bedtools, bedGraphToBigWig and bedToBigBed from bioconda), using
# Miniforge so only conda-forge/bioconda channels are involved. JupyterLab is
# included so the image can serve notebooks (e.g. via galyleo --sif).
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       git \
       procps \
    && rm -rf /var/lib/apt/lists/* \
    && curl -L 'https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh' -o /tmp/miniforge.sh \
    && bash /tmp/miniforge.sh -b -p /opt/conda \
    && rm /tmp/miniforge.sh \
    && git clone --depth 1 --branch "${RBP_MAPS_VERSION}" 'https://github.com/YeoLab/rbp-maps.git' /rbp-maps \
    && /opt/conda/bin/mamba env create -y -p /opt/rbp-maps -f /rbp-maps/environment.yml \
    && /opt/rbp-maps/bin/python -m pip install --no-cache-dir /rbp-maps \
    && /opt/conda/bin/mamba install -y -p /opt/rbp-maps -c conda-forge jupyterlab ipykernel \
    && /opt/conda/bin/conda clean -afy

ENV PATH=/opt/rbp-maps/bin:${PATH}
ENV MPLBACKEND=Agg

# Set defaults for running the image.
# The ENTRYPOINT and CMD are empty to be compatible with
# CWL and WDL implementations that cannot override those values
WORKDIR /rbp-maps
ENTRYPOINT []
CMD []
