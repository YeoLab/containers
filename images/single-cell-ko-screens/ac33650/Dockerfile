################## BASE IMAGE ######################

FROM brianyee/r-jupyter:r_3.6.1_jupyterlab1.2.6_py3.7.3

################## METADATA ######################

LABEL base_image="ubuntu:16.04"
LABEL version="1"
LABEL software="R"
LABEL software.version="4.0.5"
LABEL about.summary="Repository containing all code for secondary analysis in the manuscript \"On the design of CRISPR-based single cell molecular screens,\" Hill, McFaline-Figueroa et al."
LABEL about.home="https://github.com/shendurelab/single-cell-ko-screens#enrichment-pcr"
LABEL about.documentation=""
LABEL about.license_file=""
LABEL about.license=""
LABEL about.tags="Genomics"
  
################## MAINTAINER ######################
MAINTAINER Brian Yee <brian.alan.yee@gmail.com>

RUN Rscript -e 'install.packages("BiocManager", repos = "http://cran.us.r-project.org"); \
  BiocManager::install(c( \
    "argparse", \
    "colorRamps", "dplyr", "ggplot2", "ggrepel", "glmnet", \
    "grid", "gridExtra", "Matrix", "matrixStats", \
    "parallel", "piano", "plyr", "RColorBrewer", \
    "reshape2", "scales", "stringr", "tidyr", "viridis", \
    "monocle", "readr", "glmnet", "piano" \
  ))'
  
ENV TAR="/bin/tar"
RUN Rscript -e 'devtools::install_github(repo = "thomasp85/densityClust", ref = "edfae798225b23cdeedc41367591e37648797943")'
RUN Rscript -e 'devtools::install_github(repo = "cole-trapnell-lab/DDRTree", ref = "843607a5822276010cf4d47597213e607f7477a2")'

# https://github.com/Microsoft/microsoft-r-open/issues/63
RUN Rscript -e 'remove.packages(c("curl","httr"))'
RUN Rscript -e 'IRkernel::installspec(name = "single-cell-ko-screens", displayname = "single-cell-ko-screens", user = FALSE)'

RUN conda install -y -c https://conda.anaconda.org/biocore -c bioconda -c conda-forge pip samtools numpy scipy pandas scikit-bio pysam
RUN pip install progressbar2
RUN apt-get update && apt-get install -y git
RUN cd /opt && \
  git clone https://github.com/shendurelab/single-cell-ko-screens
# https://github.com/shendurelab/single-cell-ko-screens/issues/1
COPY get_barcodes.py /opt/single-cell-ko-screens/get_barcodes.py

ENV PATH=/opt/single-cell-ko-screens:$PATH

