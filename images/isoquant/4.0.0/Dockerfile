FROM python:3.12-slim@sha256:f77ac9e44ae96ef2c90b8053ea08c31f8be030f824196b0ae4db6d462c84e51f

LABEL software="IsoQuant" \
      software.version="4.0.0" \
      about.summary="Isoform reconstruction and quantification from long RNA reads" \
      about.url="https://github.com/ablab/IsoQuant" \
      about.license="GPL-2.0-only" \
      about.tags="Genomics,long-read-RNA,isoform-discovery,isoform-quantification"

ARG ISOQUANT_URL="https://files.pythonhosted.org/packages/42/f9/28b0f11012d105f710ef9e8ecc5f6482baf3fc854630260af8e6d211deaf/isoquant-4.0.0.tar.gz"
ARG ISOQUANT_SHA256="68fa634646525abcc6ca159f18924e430fe28455b646e9a6f49fac8bcc319293"

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates curl minimap2 samtools zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$ISOQUANT_URL" -o /tmp/isoquant.tar.gz \
    && echo "$ISOQUANT_SHA256  /tmp/isoquant.tar.gz" | sha256sum -c - \
    && pip install --no-cache-dir /tmp/isoquant.tar.gz \
    && rm /tmp/isoquant.tar.gz \
    && apt-get purge -y --auto-remove build-essential zlib1g-dev

RUN isoquant --test \
    && rm -rf /tmp/isoquant_test /isoquant_test

WORKDIR /work
ENTRYPOINT ["isoquant"]
CMD ["--help"]
