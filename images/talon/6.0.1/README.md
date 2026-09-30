# TALON 6.0.1

This image is pinned to the official BioContainers image for the latest tagged
TALON release's exact Bioconda build. Upstream's Python distribution metadata
still reports 5.0, while the tag, Bioconda package, and image version are
6.0.1.

```bash
docker run --rm -it -v "$PWD:/work" ghcr.io/yeolab/talon:6.0.1
```

The build checks every main TALON command and initializes a SQLite database
from a synthetic two-exon annotation, then verifies its transcript table.

Upstream: <https://github.com/mortazavilab/TALON>
