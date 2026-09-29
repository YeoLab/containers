# Bambu 3.14.0

This image installs Bambu 3.14.0 from Bioconductor 3.23 on R 4.6.

```bash
docker run --rm -it -v "$PWD:/work" ghcr.io/yeolab/bambu:3.14.0
```

The build verifies the package version and converts a synthetic two-exon GTF
into Bambu's prepared annotation representation.

Upstream: <https://bioconductor.org/packages/3.23/bioc/html/bambu.html>
