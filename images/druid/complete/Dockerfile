# syntax=docker/dockerfile:1
# UCSC's distributed tools are x86-64. Build with --platform linux/amd64.
FROM debian:bookworm-slim@sha256:88200866dfff7ea7f5cbcb6ec7c8a701889efe6fe859fe64d6990e4b07ea4171
ARG TARGETARCH
ARG DRUID_COMMIT=455be347cab87b62a2d1f081ec34cafffdf81622
ENV DEBIAN_FRONTEND=noninteractive LC_ALL=C.UTF-8 LANG=C.UTF-8 \
    DRUID_HOME=/opt/DRUID PATH=/opt/DRUID:/opt/DRUID/Scripts:/opt/workflow:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    THREADS=8 TMPDIR=/work/tmp
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN test "$TARGETARCH" = amd64 || { echo 'Build with --platform linux/amd64'; exit 1; }
RUN mkdir -p /work/tmp && apt-get update && apt-get install -y --no-install-recommends \
      ca-certificates curl wget git perl bash coreutils gawk parallel procps \
      samtools bedtools rna-star fastqc trimmomatic default-jre-headless \
      python3 python3-numpy python3-htseq python-is-python3 sra-toolkit \
      r-base-core r-cran-gplots r-cran-plyr r-bioc-genomicfeatures r-bioc-rtracklayer \
      libmariadb3 libpng16-16 libssl3 libuuid1 libgomp1 \
    && dpkg-query -W > /opt/debian-packages.tsv \
    && rm -rf /var/lib/apt/lists/*
RUN git init /opt/DRUID && cd /opt/DRUID \
    && git remote add origin https://github.com/risslandlab/DRUID.git \
    && git fetch --depth 1 origin "$DRUID_COMMIT" && git checkout --detach FETCH_HEAD \
    && test "$(git rev-parse HEAD)" = "$DRUID_COMMIT" \
    && echo "$DRUID_COMMIT" > /opt/DRUID/UPSTREAM_COMMIT && rm -rf .git
# Checksums intentionally fail if UCSC replaces these unversioned downloads.
RUN curl -fL --retry 5 https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa -o /usr/local/bin/twoBitToFa \
    && curl -fL --retry 5 https://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/genePredToGtf -o /usr/local/bin/genePredToGtf \
    && echo '10b2cd0d1f8208e8c0e9990b4a97d90cda4eec754b13930a10d55a40bda56710  /usr/local/bin/twoBitToFa' | sha256sum -c - \
    && echo '3596b456da9c423686a2a3f01edab9915d1969144601c0aac3c8b694375a2c18  /usr/local/bin/genePredToGtf' | sha256sum -c - \
    && chmod 755 /usr/local/bin/twoBitToFa /usr/local/bin/genePredToGtf
COPY scripts/ /opt/workflow/
COPY tests/ /opt/tests/
COPY config/ /opt/config/
RUN python3 /opt/workflow/patch_upstream.py \
    && chmod +x /opt/DRUID/*.sh /opt/DRUID/*.py /opt/DRUID/Scripts/* /opt/workflow/*.sh \
    && ln -s /usr/share/java/trimmomatic.jar /opt/trimmomatic.jar \
    && ln -s /usr/share/trimmomatic /opt/trimmomatic \
    && ln -s /opt/workflow/druid.py /usr/local/bin/druid \
    && chmod +x /opt/workflow/druid.py \
    && Rscript -e 'library(GenomicFeatures); library(rtracklayer); library(plyr); library(gplots); source("/opt/DRUID/DRUID.R"); stopifnot(is.function(DRUID))' \
    && python3 -c 'import numpy, HTSeq' \
    && STAR --version && samtools --version && bedtools --version && fastqc --version \
    && mkdir -p /work/tmp
LABEL org.opencontainers.image.title="DRUID complete analysis" \
      org.opencontainers.image.source="https://github.com/risslandlab/DRUID" \
      org.opencontainers.image.revision="455be347cab87b62a2d1f081ec34cafffdf81622"
WORKDIR /work
CMD ["bash"]
