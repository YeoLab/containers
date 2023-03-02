################## BASE IMAGE ######################

FROM jupyter/datascience-notebook:hub-2.2.2

################## METADATA ######################

LABEL base_image="jupyter/datascience-notebook:hub-2.2.2"
LABEL version="1"
LABEL software="SCAPE"
LABEL software.version="113cd0d"
LABEL about.summary="Single Cell Alternative Polyadenylation using Expectation-maximization"
LABEL about.url="https://github.com/LuChenLab/SCAPE"
LABEL about.license="MIT"
LABEL about.license_file="https://github.com/LuChenLab/SCAPE/blob/main/LICENSE"
LABEL about.publication="https://doi.org/10.1093/nar/gkac167"
LABEL about.tags="Genomics"

USER root

ARG CONDA_ENV=SCAPE

COPY apt-packages.txt /tmp/apt-packages.txt
COPY conda-packages.txt /tmp/conda-packages.txt
COPY python-packages.txt /tmp/python-packages.txt

# Update image, install additional distro packages
RUN apt-get update && xargs apt-get install -y < /tmp/apt-packages.txt

# you can add additional libraries you want mamba to install by listing them below the first line and ending with "&& \"
RUN mamba create -y -n ${CONDA_ENV} python=3.7
RUN mamba install -y -c bioconda -c conda-forge --file /tmp/conda-packages.txt -p "${CONDA_DIR}/envs/${CONDA_ENV}" && \
    mamba clean --all -f -y

RUN cd /opt && git clone https://github.com/LuChenLab/SCAPE
WORKDIR /opt/SCAPE

RUN /opt/conda/envs/${CONDA_ENV}/bin/pip install -r requirements.txt

# create Python kernel and link it to jupyter
RUN "/opt/conda/envs/${CONDA_ENV}/bin/python" -m ipykernel install --name="python3_${CONDA_ENV}" --display-name="Python3.7 ${CONDA_ENV}" && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# RUN /opt/conda/envs/${CONDA_ENV}/bin/Rscript -e 'install.packages("devtools", repos = "http://cran.us.r-project.org")'
RUN /opt/conda/envs/${CONDA_ENV}/bin/R CMD build /opt/SCAPE/SCAPE.R && /opt/conda/envs/${CONDA_ENV}/bin/Rscript -e 'install.packages("/opt/SCAPE/SCAPE_0.1.0.tar.gz", repos = NULL)'
RUN /opt/conda/envs/${CONDA_ENV}/bin/Rscript -e 'IRkernel::installspec(name = "r_${CONDA_ENV}", displayname = "R ${CONDA_ENV}")'

USER $NB_UID
ENV PATH /opt/SCAPE:/opt/conda/envs/${CONDA_ENV}/bin/:$PATH
RUN echo "conda activate ${CONDA_ENV}" >> "${HOME}/.bashrc"
