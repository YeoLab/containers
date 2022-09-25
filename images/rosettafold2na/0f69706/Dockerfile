################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="RoseTTAFold2NA"
LABEL software.version="0f697067bf41b3d4e918caa3f65803a5c6047733"
LABEL about.summary="RoseTTAFold2 protein/nucleic acid complex prediction"
LABEL about.url="https://github.com/uw-ipd/RoseTTAFold2NA"
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/uw-ipd/RoseTTAFold2NA/blob/main/LICENSE"
LABEL about.publication="https://doi.org/10.1101/2022.09.09.507333"
LABEL about.tags="Genomics"

USER root

# COPY apt-packages.txt /tmp/apt-packages.txt
# COPY conda-packages.txt /tmp/conda-packages.txt

# Update image, install additional distro packages
# RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# Install additional R packages from conda-forge using mamba
RUN cd /opt && \
  git clone https://github.com/uw-ipd/RoseTTAFold2NA.git && \
  cd /opt/RoseTTAFold2NA && \
  conda env create -f RF2na-linux.yml

RUN cd /opt/RoseTTAFold2NA/SE3Transformer && \
  pip install --no-cache-dir -r requirements.txt 

SHELL ["conda","run","-n","RF2NA","/bin/bash","-c"]

# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/RF2NA/bin/python" -m ipykernel install --name="RF2NA" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    fix-permissions "/opt/RoseTTAFold2NA"

USER $NB_UID

ENV PATH /opt/conda/envs/RF2NA/bin/:$PATH
RUN echo "conda activate RF2NA" >> "${HOME}/.bashrc"


