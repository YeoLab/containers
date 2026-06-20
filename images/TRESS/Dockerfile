# TRESS (Bioconductor devel) + Jupyter Lab with an R kernel
#
# TRESS: https://bioconductor.org/packages/devel/bioc/html/TRESS.html
# Base image already pins R to the version that matches Bioconductor devel
# and ships the system toolchain most Bioconductor packages need.
FROM bioconductor/bioconductor_docker:devel

# System deps for Jupyter (Python/pip) on top of the Bioconductor base.
RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        python3-venv \
    && rm -rf /var/lib/apt/lists/*

# Install TRESS from the Bioconductor devel branch.
# version="devel" makes BiocManager resolve against the devel repos.
RUN R -e "BiocManager::install(version = 'devel', ask = FALSE, update = FALSE)" \
    && R -e "BiocManager::install('TRESS', ask = FALSE, update = FALSE)" \
    && R -e "if (!requireNamespace('TRESS', quietly = TRUE)) quit(status = 1)"

# Jupyter Lab + the IRkernel bridge so R is selectable as a notebook kernel.
RUN pip3 install --no-cache-dir --break-system-packages jupyterlab \
    && R -e "install.packages('IRkernel', repos = 'https://cloud.r-project.org')" \
    && R -e "IRkernel::installspec(user = FALSE)"

WORKDIR /workspace
EXPOSE 8888

# Launch Jupyter Lab, reachable from the host.
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]

