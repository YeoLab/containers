# DESeq2 1.52.0

DESeq2 1.52.0 from Bioconductor 3.23 on R 4.6. The image build loads the
package and runs a small two-condition differential-expression analysis.

```bash
docker run --rm -it -v "$PWD:/work" -w /work ghcr.io/yeolab/deseq2:1.52.0
```

The default command starts R. Run an analysis script directly with:

```bash
docker run --rm -v "$PWD:/work" -w /work \
  ghcr.io/yeolab/deseq2:1.52.0 Rscript analysis.R
```
