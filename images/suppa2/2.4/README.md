# SUPPA2 2.4

SUPPA2 2.4 from the upstream GitHub release, with its Python dependencies
pinned. The upstream 2.4 tag still reports `2.3`; this image corrects that
release-string typo to `2.4` and updates SUPPA's legacy statsmodels import to
its current public location. The image build imports every dependency and
generates an isoform-event file from a small GTF.

```bash
docker run --rm ghcr.io/yeolab/suppa2:2.4 --version
docker run --rm -v "$PWD:/work" ghcr.io/yeolab/suppa2:2.4 \
  generateEvents -i /work/transcripts.gtf -o /work/events -f ioe -e SE SS MX RI FL
```

Arguments are passed directly to `suppa.py`.
