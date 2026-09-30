FROM python:3.13-slim@sha256:7c61056e61ac89e852de05f3dc6fa51a6dd2181797bceed46aa725dd7cb2cd3b

LABEL software="FLAIR" \
      software.version="3.0.1" \
      about.summary="Full-length alternative isoform analysis of RNA" \
      about.url="https://github.com/BrooksLabUCSC/flair" \
      about.license="BSD-3-Clause" \
      about.tags="Genomics,long-read-RNA,isoform-discovery,isoform-quantification"

ARG FLAIR_URL="https://files.pythonhosted.org/packages/64/c6/a5fb6bf91a36577e594753ebf97008c3536da9de0959e68343e7c5e33d5f/flair_brookslab-3.0.1.tar.gz"
ARG FLAIR_SHA256="04554034b62f95a74b1f062d5c48d39fcb21ffd122085ed7ffddb6b13de60bcf"

RUN apt-get update \
    && apt-get install -y --no-install-recommends bedtools build-essential ca-certificates curl minimap2 samtools zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$FLAIR_URL" -o /tmp/flair.tar.gz \
    && echo "$FLAIR_SHA256  /tmp/flair.tar.gz" | sha256sum -c - \
    && pip install --no-cache-dir /tmp/flair.tar.gz \
    && rm /tmp/flair.tar.gz \
    && apt-get purge -y --auto-remove build-essential zlib1g-dev

COPY verify.sh /tmp/verify.sh
RUN bash /tmp/verify.sh && rm /tmp/verify.sh

WORKDIR /work
ENTRYPOINT ["flair"]
CMD ["--help"]
