# DEXSeq 1.58.0

DEXSeq 1.58.0 from Bioconductor 3.23 on R 4.6. The image build loads the
package and constructs a small differential-exon-usage dataset.

```bash
docker run --rm -it -v "$PWD:/work" -w /work ghcr.io/yeolab/dexseq:1.58.0
```

The default command starts R. Run an analysis script directly with:

```bash
docker run --rm -v "$PWD:/work" -w /work \
  ghcr.io/yeolab/dexseq:1.58.0 Rscript analysis.R
```
