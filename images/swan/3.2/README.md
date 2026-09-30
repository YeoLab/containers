# Swan 3.2

Swan analyzes and visualizes transcript isoforms. This image installs the
latest stable PyPI release from its checksum-pinned source archive.

```bash
docker run --rm -it -v "$PWD:/work" ghcr.io/yeolab/swan:3.2
```

The build verifies the installed distribution version and loads a synthetic
two-exon GTF into a `SwanGraph`. Matplotlib uses the non-interactive `Agg`
backend so plots can be rendered on headless compute nodes.

Upstream: <https://github.com/mortazavilab/swan_vis>
