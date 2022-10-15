################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:python-3.8.13

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook"
LABEL version="1.0.0"
LABEL software="structure"
LABEL software.version="1.0.0"
LABEL about.summary="RNA structure python software/viz packages"
LABEL about.publication_forgi=""
LABEL about.license_forgi="GNU"
LABEL about.license_file_forgi="https://viennarna.github.io/forgi/license_link.html"
LABEL about.license_viennaRNA="MIT"
LABEL about.license_file_viennaRNA="https://github.com/ViennaRNA/ViennaRNA/blob/master/COPYING"
LABEL about.tags="Genomics"

USER root

COPY apt-packages.txt /tmp/apt-packages.txt
COPY python-packages.txt /tmp/python-packages.txt
# COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

#RUN conda create -c anaconda -n "structure" python=3.8 mamba cython

#SHELL ["conda", "run", "-n", "structure", "/bin/bash", "-c"]

# Install additional Python packages
RUN pip install -r /tmp/python-packages.txt

# Install additional R packages from conda-forge using mamba
# RUN mamba install -y -c conda-forge -c schrodinger -c anaconda --file /tmp/conda-packages.txt

ENV PREFIX=/opt/

RUN cd /opt && \
  git clone https://github.com/schrodinger/pymol-open-source.git && \
  git clone https://github.com/rcsb/mmtf-cpp.git && \
  mv mmtf-cpp/include/mmtf* /opt/pymol-open-source/include/ && \
  cd /opt/pymol-open-source && \
  python setup.py build --use-msgpackc=no && \
  python setup.py install --home=${PREFIX}

RUN cd /opt && \
  git clone https://github.com/ViennaRNA/forgi && \
  cd /opt/forgi && \
  python setup.py install

# RUN /opt/conda/envs/structure/bin/python -m ipykernel install --user --name python3-rnastructure-1.0.0 --display-name "Python3 (rnastructure-1.0.0)"

# RUN fix-permissions "/opt/conda/envs/structure" && \
#     fix-permissions "/home/${NB_USER}"

USER $NB_UID

# RUN echo "conda activate structure" >> ~/.bashrc
# SHELL ["/bin/bash", "--login", "-c"]
# ENV PATH=/opt/structure/:/opt/conda/envs/structure/bin:$PATH

