################## BASE IMAGE ######################

FROM nvcr.io/nvidia/cuda:11.2.2-base-centos7

################## METADATA ######################

LABEL base_image="nvcr.io/nvidia/cuda:11.2.2-base-centos7"
LABEL version="1"
LABEL software="popV"
LABEL software.version="0.0.4"
LABEL about.summary="The PopV algorithm for unsupervised label transfer from reference datasets."
LABEL about.url="https://github.com/czbiohub/PopV"
LABEL about.license=""
LABEL about.license_file=""
LABEL about.publication=""
LABEL about.tags="Genomics"

COPY yum-packages.txt /tmp/yum-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN cat /tmp/yum-packages.txt | xargs yum -y install

RUN cd /opt && wget https://ftp.gnu.org/gnu/gcc/gcc-9.2.0/gcc-9.2.0.tar.gz && \
  tar -xvf /opt/gcc-9.2.0.tar.gz && \
  cd /opt/gcc-9.2.0 && \
  ./configure --disable-multilib && \
  make && \
  make install

RUN cd /opt/ && wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
RUN cd /opt && bash Miniconda3-py39_4.9.2-Linux-x86_64.sh -b -p /opt/conda/
ENV PATH /opt/conda/bin:$PATH
RUN conda update conda;

ARG conda_env=popv

# Install additional R packages from conda-forge using mamba
RUN conda create -c bioconda -c conda-forge -c anaconda -n ${conda_env} python=3.7 cudnn cudatoolkit

# Install python packages from pip
RUN /opt/conda/envs/${conda_env}/bin/pip install -r /tmp/python-packages.txt -f https://download.pytorch.org/whl/torch_stable.html
RUN yum install -y git
RUN cd /opt && \
  git clone https://github.com/czbiohub/PopV && \
  cd /opt/PopV && \
  /opt/conda/envs/${conda_env}/bin/pip install .

# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/${conda_env}/bin/python" -m ipykernel install --name="${conda_env}"
   
ENV PATH /opt/conda/envs/${conda_env}/bin/:$PATH
RUN echo "conda activate ${conda_env}" >> "${HOME}/.bashrc"
