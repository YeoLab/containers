################## BASE IMAGE ######################

FROM ghcr.io/scverse/rapids_singlecell:latest

################## METADATA ######################

LABEL base_image="ghcr.io/scverse/rapids_singlecell:latest"
LABEL version="1"
LABEL software="rapids-singlecell"
LABEL software.version="0.10.9"
LABEL about.summary="rapids-singlecell: GPU-Accelerated Single-Cell Analysis within scverse"
LABEL about.url="https://github.com/scverse/rapids_singlecell"
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/scverse/rapids_singlecell/blob/main/LICENSE"
LABEL about.publication="https://zenodo.org/badge/latestdoi/364573913"
LABEL about.tags="Genomics"

COPY apt-packages.txt /tmp/apt-packages.txt

RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt
COPY requirements.txt /tmp/requirements.txt

# Install additional Python packages
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN pip install opencv-python
RUN python -m ipykernel install --name bento-2.1.3
