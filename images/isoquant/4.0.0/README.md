# IsoQuant 4.0.0

This image installs the latest stable IsoQuant release with minimap2 and
samtools.

```bash
docker run --rm -v "$PWD:/work" ghcr.io/yeolab/isoquant:4.0.0 --help
```

Arguments are passed directly to `isoquant`. The build runs upstream's bundled
`isoquant --test` toy-data workflow, exercising mapping, isoform discovery,
and quantification.

Upstream: <https://github.com/ablab/IsoQuant>
