################## BASE IMAGE ######################

FROM debian:trixie

################## METADATA ######################

LABEL base_image="debian:trixie"
LABEL version="1"
LABEL software="rmats-long"
LABEL software.version="v2.1.0"
LABEL about.summary="Differential isoform and alternative splicing module analysis for long-read RNA-seq"
LABEL about.url="https://github.com/Xinglab/rMATS-long"
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/Xinglab/rMATS-long/blob/main/LICENSE"
LABEL about.tags="Genomics,Transcriptomics,Long-read"

ARG RMATS_LONG_VERSION=v2.1.0

# Mirrors the upstream Dockerfile (github.com/Xinglab/rMATS-long), but pins the
# release tag and uses Miniforge (conda-forge only) so no channel ToS prompt is needed.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       git \
       procps \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /conda \
    && cd /conda \
    && curl -L 'https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh' -o miniforge.sh \
    && bash miniforge.sh -b -p /conda/install \
    && rm miniforge.sh \
    && /conda/install/bin/conda init \
    && git clone --depth 1 --branch "${RMATS_LONG_VERSION}" 'https://github.com/Xinglab/rMATS-long.git' /rMATS-long \
    && cd /rMATS-long \
    && ./install \
    && /conda/install/bin/conda clean -afy

ENV PATH=/rMATS-long/conda_env/bin:${PATH}

# Set defaults for running the image.
# The ENTRYPOINT and CMD are empty to be compatible with
# CWL and WDL implementations that cannot override those values
WORKDIR /rMATS-long
ENTRYPOINT []
CMD []
