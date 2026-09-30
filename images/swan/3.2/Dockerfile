FROM python:3.10-slim@sha256:9d53d8d4c0e882f61913025db53b3aec4ef74336082a9ab47d8a14e9e8329b00

LABEL software="Swan" \
      software.version="3.2" \
      about.summary="Analysis and visualization of transcript isoforms" \
      about.url="https://github.com/mortazavilab/swan_vis" \
      about.license="MIT" \
      about.tags="Genomics,long-read-RNA,transcript-visualization"

ARG SWAN_URL="https://files.pythonhosted.org/packages/39/8e/153cc2311f3b7e3888540a18689673b312b3e72c68ef65cce9f7c482f8ed/swan_vis-3.2.tar.gz"
ARG SWAN_SHA256="b7da08a52cc37592378428f72a22a7e994af8d63118c8949c2b758b5dfc7c1db"

ENV MPLBACKEND=Agg

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl gcc g++ \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$SWAN_URL" -o /tmp/swan.tar.gz \
    && echo "$SWAN_SHA256  /tmp/swan.tar.gz" | sha256sum -c - \
    && pip install --no-cache-dir "numpy==1.26.4" \
    && pip install --no-cache-dir /tmp/swan.tar.gz \
    && rm /tmp/swan.tar.gz \
    && apt-get purge -y --auto-remove gcc g++

COPY verify.py /tmp/verify.py
RUN python /tmp/verify.py && rm /tmp/verify.py

WORKDIR /work
CMD ["python"]
