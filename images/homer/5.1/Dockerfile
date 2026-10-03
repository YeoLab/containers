# HOMER 5.1 with bedtools and Python 3 for de novo motif discovery in CLIP
# peaks against region-matched random backgrounds (FASTA mode, -rna). Used by
# skipper-clipper-snakemake's homer_motifs rule, which follows
# yeolab/clip_analysis_legacy's analyze_motifs.

FROM mambaorg/micromamba:2.9.0-debian12-slim@sha256:edce84d758b6c3029cebdf2777d9cdfdd6e44f9eee0a31c6a09a7df14be17fd2

LABEL software="homer"
LABEL software.version="5.1"
LABEL about.summary="HOMER motif discovery with bedtools and Python 3"
LABEL about.url="http://homer.ucsd.edu/homer/"
LABEL about.tags="Genomics,motifs,eCLIP"

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml
RUN micromamba install -y -n base -f /tmp/environment.yml \
    && micromamba clean --all --yes

# Tools resolve on PATH without micromamba's activating entrypoint, as they
# must when Snakemake runs this image through Singularity/Apptainer.
ENV PATH=/opt/conda/bin:$PATH

# Fail the build if HOMER cannot find motifs in FASTA mode.
RUN printf '>a\nACGTACGTTTTTACGT\n>b\nACGTACGTTTTTACGT\n' > /tmp/fg.fa \
    && printf '>c\nGGCCGGCCAAAAGGCC\n>d\nGGCCGGCCAAAAGGCC\n' > /tmp/bg.fa \
    && findMotifs.pl /tmp/fg.fa fasta /tmp/homer-check -rna -len 6 -S 2 -p 1 \
        -nofacts -noconvert -nogo -fasta /tmp/bg.fa > /dev/null 2>&1 \
    && test -s /tmp/homer-check/homerMotifs.all.motifs \
    && rm -rf /tmp/fg.fa /tmp/bg.fa /tmp/homer-check \
    && bedtools --version && python3 --version
