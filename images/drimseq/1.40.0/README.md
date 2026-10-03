# DRIMSeq 1.40.0

DRIMSeq 1.40.0 from Bioconductor 3.23 on R 4.6. The image build loads the
package and validates construction and filtering of a small transcript-count
dataset.

```bash
docker run --rm -it -v "$PWD:/work" -w /work ghcr.io/yeolab/drimseq:1.40.0
```

The default command starts R. Run an analysis script directly with:

```bash
docker run --rm -v "$PWD:/work" -w /work \
  ghcr.io/yeolab/drimseq:1.40.0 Rscript analysis.R
```
