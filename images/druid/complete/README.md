# DRUID complete-analysis image

Singularity-ready command-line image for the [DRUID complete-analysis tutorial](https://github.com/risslandlab/DRUID/wiki/Complete-analysis), pinned to upstream commit `455be347cab87b62a2d1f081ec34cafffdf81622`.

This guide assumes a cluster where Docker is unavailable. Singularity runs the
published OCI image without a Docker daemon. Your project directory is bound
at `/work`; input data, references, temporary files, and analysis outputs stay
in that directory. The image contains software only.

## Published image

GitHub Actions builds this directory from `YeoLab/containers` and publishes
`ghcr.io/yeolab/druid:complete` plus `ghcr.io/yeolab/druid:sha-<full-commit-sha>`
after the end-to-end tests pass. All supporting-file changes trigger CI. Pull
the tested revision used by this guide on a login node or any node with network
access:

```bash
singularity pull druid.sif docker://ghcr.io/yeolab/druid:sha-7941ba6aebf0fd4beb48643ec373374b50b02bbc
export DRUID_IMAGE="$PWD/druid.sif"
```

`druid.sif` is an immutable local image file. Keep it outside the analysis
directory if your cluster backs that directory up or applies a quota to it. To
build the image from this repository instead, use `docker compose build` inside
`images/druid/complete/` on a Docker-capable development machine.

If GHCR returns an authorization error, authenticate Singularity with a GitHub
token that has `read:packages` access, or ask a package administrator to make
the package public. The repository [GHCR authentication instructions](../../../README.md#pulling-a-singularityapptainer-image-from-ghcr)
cover the login command.

## Test the pulled image

```bash
mkdir -p "$HOME/druid-smoke-test"
# Includes a small synthetic reference and all six time points, through half-life fitting.
singularity exec --cleanenv \
  --bind "$HOME/druid-smoke-test:/work" --pwd /work \
  "$DRUID_IMAGE" druid smoke-test --work /work
```

The image targets **linux/amd64**, because the bundled UCSC binaries are
x86-64. Run it on an x86-64 Linux cluster node. The smoke-test outputs are
written under `$HOME/druid-smoke-test` and can be removed after inspection.
For maintainers with Docker, a direct build is also supported:

```bash
docker build --platform linux/amd64 -t druid:complete .
```

## Run the tutorial data

Request **at least 32 GB RAM; 40 GB is recommended**, with eight CPUs from
your scheduler. The full human/fly/yeast workflow checks the effective memory
limit before running. Plan for roughly **100 GB of free working space**,
depending on BAM sizes and temporary coverage files. The six compressed FASTQs
alone total 1,615,254,957 bytes (~1.50 GiB).

Run on an allocated compute node, not a shared login node. For Slurm, a typical
interactive allocation is:

```bash
srun --pty --cpus-per-task=8 --mem=40G --time=24:00:00 bash
```

Then create or enter the directory that will hold the tutorial inputs and
outputs. Set `THREADS` to no more than the CPUs requested from the scheduler.

```bash
mkdir -p "$HOME/DRUID"
cd "$HOME/DRUID"
mkdir -p tmp logs
# Full workflow: FASTQ download -> reference construction -> QC -> trimming ->
# alignment -> HTSeq -> preDRUID -> DRUID and spike-in half-life calculations.
set -o pipefail
THREADS=8 singularity exec --cleanenv \
  --env THREADS=8,TMPDIR=/work/tmp \
  --bind "$PWD:/work" --pwd /work \
  "$DRUID_IMAGE" druid all 2>&1 | tee logs/full-analysis.log
```

The same work can be run in separate stages:

```bash
# Can run before requesting the full-memory compute allocation.
singularity exec --cleanenv --env THREADS=8,TMPDIR=/work/tmp \
  --bind "$PWD:/work" --pwd /work "$DRUID_IMAGE" druid download
# Require the full allocation for the remaining stages.
singularity exec --cleanenv --env THREADS=8,TMPDIR=/work/tmp \
  --bind "$PWD:/work" --pwd /work "$DRUID_IMAGE" druid reference
singularity exec --cleanenv --env THREADS=8,TMPDIR=/work/tmp \
  --bind "$PWD:/work" --pwd /work "$DRUID_IMAGE" druid analyze
# Repeat only the final R analysis from existing count and coverage tables.
singularity exec --cleanenv --env THREADS=8,TMPDIR=/work/tmp \
  --bind "$PWD:/work" --pwd /work "$DRUID_IMAGE" druid fit
```

`DRUID_IMAGE` records the absolute path to the file created by `singularity
pull`; use the same bind and working-directory arguments for every DRUID
command.
`--cleanenv` avoids accidentally inheriting host Python, R, or Java settings.
Samples are processed sequentially to bound memory; FastQC uses at most four
simultaneous jobs. All data are single-end, reverse-stranded, as in the
tutorial. QC reports still need scientific review.

The downloader verifies ENA MD5 checksums, skips verified existing files, and resumes `.partial` downloads. A checksum failure stops processing. If a partial file has a checksum mismatch, remove that partial file and retry. Analysis refuses to overwrite an existing `Analysis/HEK293_R1` directory; after a failed run, inspect its logs and move the directory aside before rerunning `analyze`. Reference preparation may be rerun, using cached downloads. `all` rebuilds the reference and expects a fresh analysis directory.

## Samples and reference

`config/HEK293_R1.tsv` maps the six GEO samples to ENA-hosted FASTQs from the same SRA study, **SRP108376 / PRJNA388686**. The GEO family metadata was used to verify HEK293 cells, 4SU selection, replicate 1, and treatment times. Steady-state, replicate 2, inhibitor-treated, mouse, and abnormal-spike-in samples are excluded from this tutorial run.

| Hours | Local sample | GEO | SRA run |
|---:|---|---|---|
| 1 | HEK293_R1_01 | GSM2645366 | SRR5634082 |
| 2 | HEK293_R1_02 | GSM2645367 | SRR5634083 |
| 4 | HEK293_R1_04 | GSM2645368 | SRR5634084 |
| 8 | HEK293_R1_08 | GSM2645369 | SRR5634085 |
| 12 | HEK293_R1_12 | GSM2645370 | SRR5634086 |
| 24 | HEK293_R1_24 | GSM2645371 | SRR5634087 |

Reference preparation downloads UCSC **hg38/refGene, dm6/refGene, and sacCer3/sgdGene**, filters canonical human/fly chromosomes, labels chromosome and feature identifiers with `h`, `f`, or `y`, merges the references, runs `process_GTF.R`, and builds a STAR index with `sjdbOverhang=50` and `genomeSAsparseD=2`. UCSC genePred tables are downloaded over HTTPS and passed to `genePredToGtf` as local files, avoiding the tutorial's remote MySQL dependency. The `bin` column is removed; the yeast-only trailing `proteinID` field is also removed to produce valid genePred input. All downloaded inputs remain under `ExternalData/Genomes`.

The final FASTA and GTF SHA-256 hashes are recorded in `provenance.json`. UCSC annotations at these URLs can change. To use archived, already filtered and species-labeled references:

```bash
singularity exec --cleanenv --env THREADS=8,TMPDIR=/work/tmp \
  --bind "$PWD:/work" --pwd /work "$DRUID_IMAGE" druid reference \
  --fasta /work/my-reference/combined.fa --gtf /work/my-reference/combined.gtf
```

Do not use `--small-genome` for human references; it changes STAR index parameters specifically for tiny test genomes. The custom reference must retain the tutorial's chromosome/species suffix and exon identifier conventions.

## Outputs

`Analysis/HEK293_R1/` contains:

- `FastQC/`, `TrimmedReads/`, `STAR/`, indexed `BAM/`, and `Logs/Logs.tsv`.
- `htseq_exons_introns/combined_exon.txt` and `combined_intron.txt`.
- `intersect/`: four coverage CSVs per sample.
- `half-lives.DRUID.csv` and `half-lives.spikeins.csv`: standard and leave-one-time-point-out estimates, in hours. Failed or negative fits can be `NA`.
- `DRUID.replicate.1.heatmap.DRUID.pdf` and `.filterIntrons.norm.csv`.
- `analysis.rds`: ordered samples, counts, coverage tables, and results.
- R session information, Debian package versions, sample manifest, and reference hashes.

The runner explicitly orders all matrices and STAR library sizes by numeric sampling time. It uses the wiki's trimming, alignment, counting, intron-coverage threshold, four-cluster selection, and k-means seed 42. As in upstream, DRUID fitting uses no cell-cycle correction; the spike-in comparison uses a 24-hour doubling time.

## Compatibility changes

The container retains original core files as `*.upstream.*` under `/opt/DRUID` and applies these documented changes:

1. Port `coverage.py` from Python 2 to Python 3, retaining per-base means, population standard deviations, feature lengths, and covered fractions. Accept quoted GTF attributes.
2. Replace the `preDRUID.sh` wrapper's relative paths and shared `/dev/shm` filenames with installed paths and isolated temporary directories under `/work/tmp`. Errors propagate, and unique mapping matches the exact `NH:i:1` tag, excluding `NH:i:10` and higher.
3. Remove the non-executable example section from the sourced `DRUID.R`.
4. Correct DRUID's normalization dimensions: divide each sample column by its library size and each intron row by its maximum. Upstream constructs an intron-by-intron matrix instead of an intron-by-time-point matrix and uses vector recycling for library-size division. This is a numerical correction, so results should not be represented as byte-identical outputs of unpatched upstream.
5. Update `process_GTF.R` to use the current GenomicFeatures `filter` argument in place of the removed `vals` argument, preserving longest-transcript selection; replace the removed `ignoreSelf` overlap argument by explicit diagonal-hit removal.
6. Use a command-line driver in place of manual wiki steps and hard-coded batch helpers. STAR uses `NoSharedMemory`, a 4 GB BAM-sort buffer, and disk temporary files for container compatibility. The biological filtering parameters remain as documented.

The image uses Debian Bookworm's R/Bioconductor, STAR, HTSeq, samtools, bedtools, FastQC, Trimmomatic, GNU Parallel, and SRA Toolkit. It pins the base image digest, DRUID commit, and UCSC binary checksums. Debian package updates remain possible on rebuild; `/opt/debian-packages.tsv` records exact installed versions. A UCSC download changing will fail its checksum verification rather than silently replacing the binary.

This is a runnable implementation of the tutorial with modern dependencies, not a claim of exact reproduction of the 2018 paper. The paper used a modified STAR 2.5.2a and historical annotations; its methods also describe manual intron-cluster selection, while the public script/tutorial selects a cluster automatically. The full published-data run requires the memory allocation above. See `VALIDATION.md` for the actual checks performed.

## Sources

- [DRUID source and MIT license](https://github.com/risslandlab/DRUID)
- [Complete-analysis tutorial](https://github.com/risslandlab/DRUID/wiki/Complete-analysis)
- [GEO GSE99517](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE99517)
- [ENA study SRP108376](https://www.ebi.ac.uk/ena/browser/view/SRP108376)
- [Lugowski et al., DRUID paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5900561/)

Upstream-derived code is covered by `LICENSE-DRUID`. Other included tools retain their respective licenses.
