# FLAIR 3.0.1

This image installs the latest stable FLAIR release plus its external runtime
tools: minimap2 (2.30 official release; Debian's 2.27 package omits MD tags), samtools,
and bedtools.

```bash
docker run --rm -v "$PWD:/work" ghcr.io/yeolab/flair:3.0.1 --help
```

Arguments are passed directly to `flair`. The build checks all companion
executables and performs a BED-to-GTF conversion.

Upstream: <https://github.com/BrooksLabUCSC/flair>
