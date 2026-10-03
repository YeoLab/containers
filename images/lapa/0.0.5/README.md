# LAPA 0.0.5

This image installs the latest stable LAPA release from its checksum-pinned
PyPI source archive.

```bash
docker run --rm -v "$PWD:/work" ghcr.io/yeolab/lapa:0.0.5 --help
```

Arguments are passed directly to `lapa`. The build also checks `lapa_tss` and
performs LAPA's peak selection on a synthetic transcript-end cluster.

Upstream: <https://github.com/mortazavilab/lapa>
