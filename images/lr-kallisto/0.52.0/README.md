# lr-kallisto 0.52.0

The PacBio note's lr-kallisto link now points to the main kallisto project.
This image uses kallisto 0.52.0's official checksum-pinned `LongKmer` Linux
artifact, which supports long k-mers for long-read quantification.

```bash
docker run --rm -v "$PWD:/work" ghcr.io/yeolab/lr-kallisto:0.52.0 version
```

Arguments are passed directly to `kallisto`. The build creates a 63-mer index
and quantifies a synthetic single read.

Upstream: <https://github.com/pachterlab/kallisto>
