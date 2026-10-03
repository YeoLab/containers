# skipper-clipper-compare 1.0.0

Python environment for `workflow/scripts/compare_skipper_clipper.py` in
[skipper-clipper-snakemake](https://github.com/byee4/skipper-clipper-snakemake),
which compares Skipper enriched windows with CLIPper peaks. The image holds the
environment only; the workflow supplies the script.

Pinned in `environment.yml`: Python 3.12, bedtools 2.31.1, pybedtools 0.12.0,
pandas 2.2.3, numpy 2.2.6, scipy 1.15.2, matplotlib 3.10.3, seaborn 0.13.2, and
matplotlib-venn 1.1.2. Everything is on `PATH` without activation, so the image
works under Singularity/Apptainer:

```bash
apptainer exec docker://ghcr.io/yeolab/skipper-clipper-compare:1.0.0 \
    python compare_skipper_clipper.py --help
```
