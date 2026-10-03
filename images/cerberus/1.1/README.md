# Cerberus 1.1

This image installs the latest Cerberus tag from a checksum-pinned source
archive. Upstream's placeholder package version is normalized to 1.1 so the
installed metadata agrees with the immutable tag.
The image also carries a compatibility patch that preserves strand
metadata when Cerberus reconstructs a PyRanges object with PyRanges 0.1.4.

```bash
docker run --rm -v "$PWD:/work" ghcr.io/yeolab/cerberus:1.1 --help
```

Arguments are passed directly to `cerberus`. The build converts a synthetic
two-exon GTF to both TSS BED and intron-chain TSV outputs.

Upstream: <https://github.com/mortazavilab/cerberus>
