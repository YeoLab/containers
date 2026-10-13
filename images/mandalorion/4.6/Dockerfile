FROM python:3.10-slim@sha256:9d53d8d4c0e882f61913025db53b3aec4ef74336082a9ab47d8a14e9e8329b00

LABEL software="Mandalorion" \
      software.version="4.6" \
      about.summary="Long-read isoform identification and quantification" \
      about.url="https://github.com/christopher-vollmers/Mandalorion" \
      about.license="MIT" \
      about.tags="Genomics,long-read-RNA,isoforms"

ARG MANDALORION_COMMIT=9bcfb94497b0ba1d11ebbaacac2089fd18b5aebc
ARG MINIMAP2_COMMIT=79c9cc186b95f50bd899f69b48eba995ced810c6

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential ca-certificates curl git zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && git clone https://github.com/christopher-vollmers/Mandalorion.git /opt/Mandalorion \
    && cd /opt/Mandalorion \
    && git checkout "$MANDALORION_COMMIT" \
    && git clone https://github.com/lh3/minimap2.git minimap2 \
    && cd minimap2 \
    && git checkout "$MINIMAP2_COMMIT" \
    && make -j2 \
    && cd /opt/Mandalorion \
    && curl -fsSL https://github.com/yangao07/abPOA/releases/download/v1.4.1/abPOA-v1.4.1.tar.gz -o /tmp/abpoa.tar.gz \
    && tar -xzf /tmp/abpoa.tar.gz \
    && make -C abPOA-v1.4.1 -j2 sse2=1 \
    && python -m pip install --no-cache-dir 'numpy<2' mappy 'matplotlib<4' editdistance \
    && python Mando.py --version \
    && test -x minimap2/minimap2 \
    && test -x abPOA-v1.4.1/bin/abpoa \
    && rm /tmp/abpoa.tar.gz

ENV PATH=/opt/Mandalorion:/opt/Mandalorion/minimap2:/opt/Mandalorion/abPOA-v1.4.1/bin:$PATH
WORKDIR /work
CMD ["python", "/opt/Mandalorion/Mando.py", "--help"]
