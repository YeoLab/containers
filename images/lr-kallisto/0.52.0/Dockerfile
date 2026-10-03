FROM debian:bookworm-slim@sha256:3783cc01769c7b2b1b83a5c5ad96c815348e28ed7da68e2e3687004faa906251

LABEL software="lr-kallisto" \
      software.version="0.52.0" \
      about.summary="Long-read pseudoalignment and transcript quantification with kallisto" \
      about.url="https://github.com/pachterlab/kallisto" \
      about.license="BSD-2-Clause" \
      about.tags="Genomics,long-read-RNA,isoform-quantification"

ARG KALLISTO_URL="https://github.com/pachterlab/kallisto/releases/download/v0.52.0/kallisto_linux_LongKmer-v0.52.0.tar.gz"
ARG KALLISTO_SHA256="88ea2e1f76537d2c866d54a2b9f7d2d4fa6ef095712b0da3cb65ebd74bc7b30c"

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$KALLISTO_URL" -o /tmp/kallisto.tar.gz \
    && echo "$KALLISTO_SHA256  /tmp/kallisto.tar.gz" | sha256sum -c - \
    && tar -xzf /tmp/kallisto.tar.gz -C /tmp \
    && install -m 0755 /tmp/kallisto/kallisto /usr/local/bin/kallisto \
    && rm -rf /tmp/kallisto /tmp/kallisto.tar.gz

COPY verify.sh /tmp/verify.sh
RUN bash /tmp/verify.sh && rm /tmp/verify.sh

WORKDIR /work
ENTRYPOINT ["kallisto"]
CMD ["version"]
