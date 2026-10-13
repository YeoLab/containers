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

# The bundled gtfToGenePred links against libbz2.so.1, but the image only provides
# the libbz2.so.1.0 soname; without it sqanti3_qc.py fails at GTF to genePred conversion.
RUN ln -s libbz2.so.1.0.8 /usr/local/lib/libbz2.so.1

COPY verify.py /tmp/verify.py
RUN python /tmp/verify.py && rm /tmp/verify.py

WORKDIR /work
ENTRYPOINT []
CMD ["bash"]
