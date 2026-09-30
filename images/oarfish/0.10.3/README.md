# Oarfish 0.10.3

This image installs the latest stable Oarfish Linux release from its official
checksum-pinned binary archive.

```bash
docker run --rm -v "$PWD:/work" ghcr.io/yeolab/oarfish:0.10.3 --help
```

Arguments are passed directly to `oarfish`. The build verifies the version and
constructs an Oarfish index from a synthetic transcriptome.

Upstream: <https://github.com/COMBINE-lab/oarfish>
