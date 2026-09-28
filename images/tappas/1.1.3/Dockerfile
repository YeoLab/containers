FROM bioconductor/bioconductor_docker:RELEASE_3_23@sha256:821dbf9ac119eac41f177531c7ca8fc7084c99c04eb218a1aa7f52cb63bad5d9

LABEL software="tappAS" \
      software.version="1.1.3" \
      about.summary="Functional analysis of alternative transcript expression mechanisms" \
      about.url="https://github.com/ConesaLab/tappAS" \
      about.license="GPL-3.0-or-later" \
      about.tags="Genomics,RNA-seq,alternative-splicing,GUI"

ARG TAPPAS_URL="https://github.com/ConesaLab/tappAS/releases/download/v1.1.3/tappAS-linux.zip"
ARG TAPPAS_SHA256="fa7eda0072610412acbb8a21281a2c563a69fc39255dce632f72690996643761"
ARG GOGLM_REF="e4d3f462b30514b9df9c6765c91ea2042439dcea"

ENV GOGLM_REF=${GOGLM_REF}

USER root

RUN test "$(uname -m)" = "x86_64" \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      libasound2t64 \
      libgl1 \
      libgtk-3-0t64 \
      libxi6 \
      libxrender1 \
      libxtst6 \
      unzip \
      xvfb \
    && rm -rf /var/lib/apt/lists/* \
    && curl -fsSL "$TAPPAS_URL" -o /tmp/tappas.zip \
    && echo "$TAPPAS_SHA256  /tmp/tappas.zip" | sha256sum -c - \
    && unzip -q /tmp/tappas.zip -d /tmp/tappas-release \
    && mv /tmp/tappas-release/dist/linux/tappas /opt/tappas \
    && rm -rf /tmp/tappas.zip /tmp/tappas-release \
    && sed -i 's/java-options=-Xms8g/java-options=-Xms2g/' /opt/tappas/lib/app/tappas.cfg \
    && ln -s /opt/tappas/bin/tappas /usr/local/bin/tappas \
    && ln -s /usr/local/bin/Rscript /usr/bin/Rscript \
    && printf '%s\n' '1.1.3' > /opt/tappas/VERSION

RUN Rscript -e 'BiocManager::install(c("DEXSeq", "edgeR", "NOISeq", "goseq", "maSigPro"), ask = FALSE, update = FALSE)'

RUN Rscript -e 'install.packages(c("callr", "devtools", "ggpubr", "ggplot2", "MASS", "plyr", "remotes", "VennDiagram", "ggrepel", "cowplot", "tidyverse", "UpSetR"))'

RUN Rscript -e 'remotes::install_github("gu-mi/GOglm", ref = Sys.getenv("GOGLM_REF"), upgrade = "never")'

COPY verify.R /tmp/verify.R
RUN Rscript /tmp/verify.R \
    && test "$(cat /opt/tappas/VERSION)" = "1.1.3" \
    && unzip -l /opt/tappas/lib/app/tappas-jar-with-dependencies.jar | grep -q 'tappas/Tappas.class' \
    && /opt/tappas/lib/runtime/bin/java -version \
    && rm /tmp/verify.R

WORKDIR /work
ENTRYPOINT ["/usr/local/bin/tappas"]
