################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="scarches"
LABEL software.version="0.5.7"
LABEL about.summary="Single-cell architecture surgery (scArches) is a package for reference-based analysis of single-cell data."
LABEL about.url="http://github.com/theislab/scarches"
LABEL about.license="BSD-3"
LABEL about.license_file="https://github.com/theislab/scarches/blob/master/LICENSE"
LABEL about.publication="https://www.nature.com/articles/s41587-021-01001-7"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN conda env config vars set SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
RUN mamba install -y -c pytorch -c nvidia -c bioconda -c conda-forge --file /tmp/conda-packages.txt

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt
RUN pip install pyg_lib torch_scatter torch_sparse -f https://data.pyg.org/whl/torch-1.13.1+cu117.html
RUN pip install torch-geometric
RUN pip install torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-1.13.1+cu117.html
RUN pip install "jax[cuda11_cudnn82]" -f https://storage.googleapis.com/jax-releases/jax_cuda_releases.html

#RUN pip install jax[cuda]>=0.4

USER $NB_UID
