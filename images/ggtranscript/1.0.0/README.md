# ggtranscript 1.0.0

ggtranscript extends ggplot2 with geoms and helpers for transcript structures.
The project has no release tags, so this image pins the current upstream
version 1.0.0 to commit `682a0df688ad242fa262d0b0557bf973dc202787`.

```bash
docker run --rm -it -v "$PWD:/work" ghcr.io/yeolab/ggtranscript:1.0.0
```

The build verifies package version 1.0.0, derives an intron from synthetic
exons, and builds a ggplot using `geom_range()`.

Upstream: <https://github.com/dzhang32/ggtranscript>
