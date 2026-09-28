FROM python:3.13-slim@sha256:7c61056e61ac89e852de05f3dc6fa51a6dd2181797bceed46aa725dd7cb2cd3b

LABEL software="SUPPA2" \
      software.version="2.4" \
      about.summary="Differential splicing and transcript usage analysis" \
      about.url="https://github.com/comprna/SUPPA" \
      about.license="MIT" \
      about.tags="Genomics,RNA-seq,alternative-splicing"

ARG SUPPA_URL="https://github.com/comprna/SUPPA/archive/refs/tags/v2.4.tar.gz"
ARG SUPPA_SHA256="a71b3017dd13ceb4b8b837dfae201eb3bc55fb11dfcb201434f6ff1e4733093c"

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$SUPPA_URL" -o /tmp/suppa.tar.gz \
    && echo "$SUPPA_SHA256  /tmp/suppa.tar.gz" | sha256sum -c - \
    && mkdir -p /opt/suppa \
    && tar -xzf /tmp/suppa.tar.gz --strip-components=1 -C /opt/suppa \
    && rm /tmp/suppa.tar.gz \
    && sed -i "s/version='%(prog)s 2.3'/version='%(prog)s 2.4'/" /opt/suppa/suppa.py \
    && sed -i 's/from statsmodels\.sandbox\.stats\.multicomp import multipletests/from statsmodels.stats.multitest import multipletests/' /opt/suppa/lib/diff_tools.py \
    && ln -s /opt/suppa/suppa.py /usr/local/bin/suppa.py \
    && chmod +x /opt/suppa/suppa.py

RUN pip install --no-cache-dir \
      matplotlib==3.11.2 \
      numpy==2.5.3 \
      pandas==3.0.6 \
      scikit-learn==1.9.1 \
      scipy==1.18.1 \
      statsmodels==0.15.0

COPY verify.sh /tmp/verify.sh
RUN bash /tmp/verify.sh && rm /tmp/verify.sh

WORKDIR /work
ENTRYPOINT ["python3", "/opt/suppa/suppa.py"]
CMD ["--help"]
