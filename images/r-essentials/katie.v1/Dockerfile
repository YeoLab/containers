# Use the latest Jupyter R-notebook as the base image
FROM jupyter/r-notebook:latest

WORKDIR /home/jovyan/work

# STEP 1: Install heavy C++ packages and specific dependencies via Mamba
# We explicitly install 'fgsea', 'ggtree', and 'shadowtext' via Conda binaries 
# because they are the root cause of the source compilation failures in R.
# We EXCLUDE clusterprofiler, enrichplot, and dose to avoid the go.db Conda trap.
RUN mamba install --quiet --yes \
    -c conda-forge -c bioconda \
    'bioconductor-deseq2' \
    'bioconductor-tximport' \
    'bioconductor-ihw' \
    'bioconductor-apeglm' \
    'bioconductor-enhancedvolcano' \
    'bioconductor-fgsea' \
    'bioconductor-ggtree' \
    'r-shadowtext' \
    'r-pheatmap' \
    'r-rcolorbrewer' \
    'r-ggplot2' \
    'r-ggrepel' && \
    mamba clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"

# STEP 2: Install annotation databases and their dependents natively via R
# BiocManager handles these perfectly without the broken Conda post-link scripts.
RUN Rscript -e "if (!requireNamespace('BiocManager', quietly = TRUE)) install.packages('BiocManager', repos='https://cloud.r-project.org')" && \
    Rscript -e "BiocManager::install(c('DOSE', 'enrichplot', 'clusterProfiler', 'org.Hs.eg.db'), update = FALSE, ask = FALSE)"
