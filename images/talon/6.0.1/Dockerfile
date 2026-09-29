FROM quay.io/biocontainers/talon:6.0.1--pyhdfd78af_0@sha256:789e65a7506e8dac4059e479d7790f909f85279c288dac558b1272c6311cdbb2

LABEL software="TALON" \
      software.version="6.0.1" \
      about.summary="Technology-agnostic long-read isoform discovery and quantification" \
      about.url="https://github.com/mortazavilab/TALON" \
      about.license="MIT" \
      about.tags="Genomics,long-read-RNA,isoform-classification,isoform-quantification"

COPY verify.sh /tmp/verify.sh
RUN bash /tmp/verify.sh && rm /tmp/verify.sh

WORKDIR /work
ENTRYPOINT []
CMD ["talon", "--help"]
