################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="popV"
LABEL software.version="0.0.4"
LABEL about.summary="The PopV algorithm for unsupervised label transfer from reference datasets."
LABEL about.url="https://github.com/czbiohub/PopV"
LABEL about.license=""
LABEL about.license_file=""
LABEL about.publication=""
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

ARG conda_env=popv

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN conda create -c bioconda -c conda-forge -c anaconda -n ${conda_env} python=3.7 cudnn=8.2.1.32 cudatoolkit=11.0.221

# Install python packages from pip
RUN /opt/conda/envs/${conda_env}/bin/pip install -r /tmp/python-packages.txt -f https://download.pytorch.org/whl/torch_stable.html

RUN cd /opt && \
  git clone https://github.com/czbiohub/PopV && \
  cd /opt/PopV && \
  /opt/conda/envs/${conda_env}/bin/python setup.py install

# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/${conda_env}/bin/python" -m ipykernel install --name="${conda_env}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
    
USER $NB_UID
ENV PATH /opt/conda/envs/${conda_env}/bin/:$PATH
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"
