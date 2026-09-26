# HOMER 5.1

[HOMER](http://homer.ucsd.edu/homer/) 5.1 with bedtools 2.31.1 and Python 3.12,
pinned in `environment.yml`. No genome packages are installed: it is meant for
FASTA-mode motif finding (`findMotifs.pl <fg.fa> fasta <out> -fasta <bg.fa>`),
as used by
[skipper-clipper-snakemake](https://github.com/byee4/skipper-clipper-snakemake)'s
`homer_motifs` rule. Everything is on `PATH` without activation, so it runs under
Singularity/Apptainer:

```bash
apptainer exec docker://ghcr.io/yeolab/homer:5.1 findMotifs.pl
```
