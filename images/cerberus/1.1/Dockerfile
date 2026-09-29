FROM python:3.10-slim@sha256:9d53d8d4c0e882f61913025db53b3aec4ef74336082a9ab47d8a14e9e8329b00

LABEL software="Cerberus" \
      software.version="1.1" \
      about.summary="Transcript start, end, and intron-chain annotation" \
      about.url="https://github.com/mortazavilab/cerberus" \
      about.license="MIT" \
      about.tags="Genomics,long-read-RNA,isoform-classification"

ARG LAPA_URL="https://files.pythonhosted.org/packages/64/cc/e9059f9e9108f5a9a22e08164e29be3a937bab6c7636a8c2e51bf5b85ceb/lapa-0.0.5.tar.gz"
ARG LAPA_SHA256="3240405cbdd0e68c344676bc780e62368359024726f0ef2c04ef487d49793669"
ARG SWAN_URL="https://files.pythonhosted.org/packages/39/8e/153cc2311f3b7e3888540a18689673b312b3e72c68ef65cce9f7c482f8ed/swan_vis-3.2.tar.gz"
ARG SWAN_SHA256="b7da08a52cc37592378428f72a22a7e994af8d63118c8949c2b758b5dfc7c1db"
ARG CERBERUS_URL="https://github.com/mortazavilab/cerberus/archive/refs/tags/v1.1.tar.gz"
ARG CERBERUS_SHA256="c1693ef8ab48cdf841e769eb49d5d957b1d426635a6f7fdfe162914673d7de9f"

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates curl patch \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$LAPA_URL" -o /tmp/lapa.tar.gz \
    && echo "$LAPA_SHA256  /tmp/lapa.tar.gz" | sha256sum -c - \
    && curl -fsSL "$SWAN_URL" -o /tmp/swan.tar.gz \
    && echo "$SWAN_SHA256  /tmp/swan.tar.gz" | sha256sum -c - \
    && pip install --no-cache-dir \
        "numpy==1.23.0" \
        "pandas==1.5.3" \
        "scipy==1.10.1" \
        "matplotlib==3.7.5" \
        "h5py==3.8.0" \
        "blosc2==2.0.0" \
        "tables==3.8.0" \
        "pandarallel==1.6.5" \
        "anndata==0.9.2" \
        "scanpy==1.9.8" \
        "numba==0.57.1" \
        "scikit-learn==1.3.2" \
        "umap-learn==0.5.5" \
        "sparse==0.14.0" \
        "python-ternary==1.0.8" \
        "cython<3" \
    && pip install --no-cache-dir --no-build-isolation "sorted-nearest==0.0.33" \
    && pip install --no-cache-dir "pyranges==0.1.4" \
    && pip install --no-cache-dir /tmp/lapa.tar.gz \
    && pip install --no-cache-dir /tmp/swan.tar.gz \
    && rm -rf /tmp/lapa.tar.gz /tmp/swan.tar.gz \
    && apt-get purge -y --auto-remove build-essential

COPY pyranges-compat.patch /tmp/pyranges-compat.patch

RUN curl -fsSL "$CERBERUS_URL" -o /tmp/cerberus.tar.gz \
    && echo "$CERBERUS_SHA256  /tmp/cerberus.tar.gz" | sha256sum -c - \
    && mkdir /tmp/cerberus \
    && tar -xzf /tmp/cerberus.tar.gz --strip-components=1 -C /tmp/cerberus \
    && sed -i "s/version='0.0.idk'/version='1.1'/" /tmp/cerberus/setup.py \
    && patch -d /tmp/cerberus -p1 < /tmp/pyranges-compat.patch \
    && pip install --no-cache-dir --no-deps /tmp/cerberus \
    && rm -rf /tmp/cerberus.tar.gz /tmp/cerberus /tmp/pyranges-compat.patch \
    && apt-get purge -y --auto-remove curl patch

COPY verify.sh /tmp/verify.sh
RUN bash /tmp/verify.sh && rm /tmp/verify.sh

WORKDIR /work
ENTRYPOINT ["cerberus"]
CMD ["--help"]
