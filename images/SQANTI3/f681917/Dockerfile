################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.0.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.0.2"
LABEL version="1"
LABEL software="SQANTI3"
LABEL software.version="f681917f745ad76a7b90ab6c5dcc677ce0b25231"
LABEL about.summary="Tool for the Quality Control of Long-Read Defined Transcriptomes"
LABEL about.url="https://github.com/ConesaLab/SQANTI3"
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/ConesaLab/SQANTI3/blob/master/LICENSE.md"
LABEL about.publication="doi:10.1101/gr.222976.117"
LABEL about.tags="Genomics"

USER root

# Update image, install additional distro packages
RUN apt-get update && apt-get install gcc

# include more dependencies that are needed
COPY SQANTI3.conda_env.yml /tmp/SQANTI3.conda_env.yml

RUN cd /opt && \
  git clone https://github.com/ConesaLab/SQANTI3 && \
  cd /opt/SQANTI3 && \
  git checkout f681917f745ad76a7b90ab6c5dcc677ce0b25231 && \
  conda env create -n "SQANTI3.env" -f /tmp/SQANTI3.conda_env.yml 

# gtfToGenePred already in utilities folder
# RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/gtfToGenePred -P /opt/SQANTI3/utilities/ && \
#   chmod +x /opt/SQANTI3/utilities/gtfToGenePred 

SHELL ["conda","run","-n","SQANTI3.env","/bin/bash","-c"]

RUN Rscript -e "devtools::install_github(\"ConesaLab/RColorConesa\")"

RUN cd /opt && \
  git clone https://github.com/Magdoll/cDNA_Cupcake.git && \
  cd /opt/cDNA_Cupcake && \
  python setup.py build && \
  python setup.py install

RUN fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}" && \
    fix-permissions "/opt/SQANTI3"

USER $NB_UID

RUN echo "conda activate SQANTI3.env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]
ENV PATH=/opt/SQANTI3/:$PATH

