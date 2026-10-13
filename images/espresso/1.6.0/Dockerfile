FROM mambaorg/micromamba:2.9.0-debian12-slim@sha256:edce84d758b6c3029cebdf2777d9cdfdd6e44f9eee0a31c6a09a7df14be17fd2

LABEL software="ESPRESSO" \
      software.version="1.6.0" \
      about.summary="Long-read splice junction correction and isoform quantification" \
      about.url="https://github.com/Xinglab/espresso" \
      about.tags="Genomics,long-read-RNA,isoforms"

ARG ESPRESSO_COMMIT=69b54b70470ceb133472e0448fe64783be011e53

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates git make \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/Xinglab/espresso.git /opt/espresso \
    && cd /opt/espresso \
    && git checkout "$ESPRESSO_COMMIT" \
    && chown -R "$MAMBA_USER:$MAMBA_USER" /opt/espresso

USER $MAMBA_USER
RUN micromamba install -y -n base -c conda-forge -c bioconda \
        --file /opt/espresso/snakemake/conda_requirements.txt \
    && micromamba clean --all --yes

# The upstream Snakemake wrapper activates conda from ~/.bashrc. Its commands
# already resolve in this image, including under Singularity without an entrypoint.
ENV PATH=/opt/conda/bin:$PATH
RUN cd /opt/espresso \
    && src/Parasail/build \
    && cp src/Parasail/libparasail.so snakemake/scripts/libparasail.so \
    && printf '#!/bin/sh\nexec "$@"\n' > snakemake/conda_wrapper \
    && chmod +x snakemake/conda_wrapper \
    && printf '\nconda_wrapper: /opt/espresso/snakemake/conda_wrapper\nespresso_path: /opt/espresso/src\nvisualization_path: /opt/espresso/visualization\nlibparasail_so_path: /opt/espresso/snakemake/scripts/libparasail.so\n' >> snakemake/snakemake_config.yaml \
    && perl -e 'use threads; use Storable; use lib "/opt/espresso/src"; use Parasail; die "Storable too old\n" if $Storable::VERSION < 3' \
    && perl -c src/ESPRESSO_S.pl \
    && perl -c src/ESPRESSO_C.pl \
    && perl -c src/ESPRESSO_Q.pl \
    && snakemake --version

WORKDIR /work
CMD ["/bin/bash"]
