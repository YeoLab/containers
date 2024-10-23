################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="scanpy"
LABEL software.version="1.10.3"
LABEL about.summary="Single-Cell Analysis in Python. Scales to >1M cells."
LABEL about.url="http://github.com/theislab/scanpy"
LABEL about.license="BSD-3"
LABEL about.license_file="https://github.com/theislab/scanpy/blob/master/LICENSE"
LABEL about.publication="https://doi.org/10.1186/s13059-017-1382-0"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt

#
RUN pip install llvmlite --ignore-installed
# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

# RUN Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN Rscript -e 'devtools::install_github("navinlabcode/copykat")'

RUN cd /opt && \
	git clone https://github.com/theislab/diffxpy && \
	cd diffxpy && \
        pip install -e .

USER $NB_UID
