FROM debian:bookworm-slim@sha256:3783cc01769c7b2b1b83a5c5ad96c815348e28ed7da68e2e3687004faa906251

LABEL software="Oarfish" \
      software.version="0.10.3" \
      about.summary="Fast and accurate long-read transcript quantification" \
      about.url="https://github.com/COMBINE-lab/oarfish" \
      about.license="BSD-3-Clause" \
      about.tags="Genomics,long-read-RNA,isoform-quantification"

ARG OARFISH_URL="https://github.com/COMBINE-lab/oarfish/releases/download/v0.10.3/oarfish-x86_64-unknown-linux-gnu.tar.xz"
ARG OARFISH_SHA256="ad23cd748ad306ea736e76670d40298ee66704bbcbcb4ddeedb301bfaee57461"

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl xz-utils \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$OARFISH_URL" -o /tmp/oarfish.tar.xz \
    && echo "$OARFISH_SHA256  /tmp/oarfish.tar.xz" | sha256sum -c - \
    && tar -xJf /tmp/oarfish.tar.xz -C /tmp \
    && install -m 0755 /tmp/oarfish-x86_64-unknown-linux-gnu/oarfish /usr/local/bin/oarfish \
    && rm -rf /tmp/oarfish-x86_64-unknown-linux-gnu /tmp/oarfish.tar.xz

COPY verify.sh /tmp/verify.sh
RUN bash /tmp/verify.sh && rm /tmp/verify.sh

WORKDIR /work
ENTRYPOINT ["oarfish"]
CMD ["--help"]
