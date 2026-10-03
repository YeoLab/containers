# Environment for skipper-clipper-snakemake's compare_skipper_clipper.py:
# Skipper enriched windows vs CLIPper peaks (pandas, pybedtools/bedtools,
# scipy, matplotlib, seaborn, matplotlib-venn). The script itself lives in the
# workflow repository and is run inside this image by the workflow.

FROM mambaorg/micromamba:2.9.0-debian12-slim@sha256:edce84d758b6c3029cebdf2777d9cdfdd6e44f9eee0a31c6a09a7df14be17fd2

LABEL software="skipper-clipper-compare"
LABEL software.version="1.0.0"
LABEL about.summary="Python environment comparing Skipper enriched windows with CLIPper peaks"
LABEL about.url="https://github.com/byee4/skipper-clipper-snakemake"
LABEL about.tags="Genomics,eCLIP"

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml \
    && micromamba clean --all --yes

# Tools resolve on PATH without micromamba's activating entrypoint, as they
# must when Snakemake runs this image through Singularity/Apptainer.
ENV PATH=/opt/conda/bin:$PATH \
    MPLBACKEND=Agg

# Fail the build, not a pipeline job, if the environment is incomplete.
RUN python -c "import pandas, numpy, scipy, matplotlib, seaborn, matplotlib_venn, pybedtools; \
from pybedtools import BedTool; \
assert len(BedTool('chr1 1 9 a 0 +', from_string=True).sort()) == 1" \
    && bedtools --version
