################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="cleanlab"
LABEL software.version="2.3.1"
LABEL about.summary="The standard package for machine learning with noisy labels and finding mislabeled data in Python."
LABEL about.url="https://github.com/cleanlab/cleanlab"
LABEL about.license="A-GPL3"
LABEL about.license_file="https://github.com/cleanlab/cleanlab/blob/master/LICENSE"
LABEL about.publication="https://arxiv.org/abs/1911.00068"
LABEL about.publication="https://arxiv.org/abs/1705.01936"
LABEL about.publication="https://people.csail.mit.edu/jonasmueller/info/LabelQuality_icml.pdf"
LABEL about.publication="https://arxiv.org/abs/2207.03061"
LABEL about.publication="https://arxiv.org/abs/2210.03920"
LABEL about.publication="https://arxiv.org/abs/2210.06812"
LABEL about.publication="https://arxiv.org/abs/2301.11856"
LABEL about.publication="https://arxiv.org/abs/2211.13895"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

USER $NB_UID
