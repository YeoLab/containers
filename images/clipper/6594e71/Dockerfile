################## BASE IMAGE ######################

FROM brianyee/clipper:42502ec

################## METADATA ######################

LABEL base_image="brianyee/miniconda_xenial:4.6.14"
LABEL version="1"
LABEL software="CLIPper"
LABEL software.version="6594e717ce5607220406c6271e4e327ecebad464"
LABEL about.summary="A tool to detect CLIP-seq peaks."
LABEL about.home="https://github.com/YeoLab/clipper/"
LABEL about.documentation="https://github.com/YeoLab/clipper/wiki/CLIPper-Home"
LABEL about.license_file="https://github.com/YeoLab/clipper/blob/master/LICENSE"
LABEL about.license="MIT"
LABEL about.tags="Genomics"

################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

RUN apt-get update

RUN cd /opt/ && \
    rm -rf clipper && \
    git clone http://github.com/yeolab/clipper && \
    cd /opt/clipper && \
    git checkout 6594e717ce5607220406c6271e4e327ecebad464

SHELL ["conda", "run", "-n", "clipper3", "/bin/bash", "-c"]

RUN cd /opt/clipper/ && \
    python setup.py install

ENV PATH /opt/conda/envs/clipper3/bin:$PATH

