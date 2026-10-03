# SQANTI3 6.0.2

This image is pinned to the official BioContainers image for SQANTI3's exact
Bioconda 6.0.2 build and includes the complete aligner, command-line, Python,
R, and report-generation stack.

```bash
docker run --rm -it -v "$PWD:/work" ghcr.io/yeolab/sqanti3:6.0.2
```

The build verifies both SQANTI3's reported version and R dependencies, checks
the external tools, and parses a synthetic two-exon genePred transcript through
SQANTI3's own parser.

Upstream: <https://github.com/ConesaLab/SQANTI3>
