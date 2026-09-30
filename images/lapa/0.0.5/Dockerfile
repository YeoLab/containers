FROM python:3.10-slim@sha256:9d53d8d4c0e882f61913025db53b3aec4ef74336082a9ab47d8a14e9e8329b00

LABEL software="LAPA" \
      software.version="0.0.5" \
      about.summary="Alternative polyadenylation and transcript-end analysis" \
      about.url="https://github.com/mortazavilab/lapa" \
      about.license="MIT" \
      about.tags="Genomics,long-read-RNA,transcript-ends"

ARG LAPA_URL="https://files.pythonhosted.org/packages/64/cc/e9059f9e9108f5a9a22e08164e29be3a937bab6c7636a8c2e51bf5b85ceb/lapa-0.0.5.tar.gz"
ARG LAPA_SHA256="3240405cbdd0e68c344676bc780e62368359024726f0ef2c04ef487d49793669"

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$LAPA_URL" -o /tmp/lapa.tar.gz \
    && echo "$LAPA_SHA256  /tmp/lapa.tar.gz" | sha256sum -c - \
    && pip install --no-cache-dir "numpy==1.23.0" "cython<3" \
    && pip install --no-cache-dir --no-build-isolation "sorted-nearest==0.0.33" \
    && pip install --no-cache-dir /tmp/lapa.tar.gz \
    && rm /tmp/lapa.tar.gz \
    && apt-get purge -y --auto-remove build-essential

COPY verify.py /tmp/verify.py
RUN python /tmp/verify.py \
    && lapa --help >/dev/null \
    && lapa_tss --help >/dev/null \
    && rm /tmp/verify.py

WORKDIR /work
ENTRYPOINT ["lapa"]
CMD ["--help"]
