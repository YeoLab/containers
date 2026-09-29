FROM quay.io/biocontainers/sqanti3:6.0.2--hdfd78af_1@sha256:3ebeb658fb2e0e308e73cba50dd3b97c63963d8225f303f298ad8ee76264939d

LABEL software="SQANTI3" \
      software.version="6.0.2" \
      about.summary="Quality control and classification of long-read transcript isoforms" \
      about.url="https://github.com/ConesaLab/SQANTI3" \
      about.license="GPL-3.0-only" \
      about.tags="Genomics,long-read-RNA,isoform-classification"

ENV MPLBACKEND=Agg \
    PYTHONPATH=/usr/local/share/sqanti3-6.0.2-1 \
    PYTHONWARNINGS=ignore::DeprecationWarning

COPY verify.py /tmp/verify.py
RUN python /tmp/verify.py && rm /tmp/verify.py

WORKDIR /work
ENTRYPOINT []
CMD ["bash"]
