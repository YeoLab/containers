################## BASE IMAGE ######################

# Built on the published 1.45 image (pushed to Docker Hub as brianyee/deseq2:1.44, 2024-07-26).
# Rebuilding the original recipe from jupyter/datascience-notebook:hub-2.2.2 no longer works:
# the conda C++ compiler cannot build BiocParallel, so DESeq2 and its dependents fail to install.
# The original recipe is in git history (commit 9fb3e66).
FROM brianyee/deseq2:1.44@sha256:4fbae75ccd105740124128564d9b5b553a968c171ec7b7ebaa6f0188ff2c7e08

################## METADATA ######################

LABEL base_image="brianyee/deseq2:1.44@sha256:4fbae75ccd105740124128564d9b5b553a968c171ec7b7ebaa6f0188ff2c7e08"
LABEL version="2"
LABEL software="deseq2"
LABEL software.version="1.45.0"
LABEL about.summary="Differential gene expression analysis based on the negative binomial distribution"
LABEL about.url="https://bioconductor.org/packages/3.16/bioc/html/DESeq2.html"
LABEL about.license="LGPL (>= 3)"
LABEL about.publication="10.1186/s13059-014-0550-8"
LABEL about.tags="Genomics"

USER root

# LFC shrinkage: lfcShrink(type = "apeglm" / "ashr")
RUN Rscript -e 'install.packages(c("emdbook", "RcppNumerical", "RcppEigen"), repos = "https://cloud.r-project.org")'
RUN Rscript -e 'devtools::install_version("ashr", version = "2.2-63", repos = "https://cloud.r-project.org", upgrade = "never")'
RUN Rscript -e 'install.packages("https://bioconductor.org/packages/3.18/bioc/src/contrib/apeglm_1.24.0.tar.gz", repos = NULL, type = "source")'
RUN Rscript -e 'install.packages("ggrepel", repos = "https://cloud.r-project.org")'
RUN Rscript -e 'install.packages("https://bioconductor.org/packages/3.18/bioc/src/contrib/EnhancedVolcano_1.20.0.tar.gz", repos = NULL, type = "source")'
# install.packages() only warns on failure: fail the build if any package is missing
RUN Rscript -e 'library(DESeq2); library(tximport); library(apeglm); library(ashr); library(EnhancedVolcano)'
#USER $NB_UID
