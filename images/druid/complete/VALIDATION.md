# Validation — 2026-09-08

The image was built and tested locally using Docker Desktop on Apple Silicon with `linux/amd64` emulation, eight available CPUs, and approximately 12 GB allocated to Docker.

## Passed

- `docker compose build`: built `druid:complete` successfully.
- `docker buildx build --check --platform linux/amd64 .`: no warnings.
- `docker compose config --quiet`: valid Compose configuration.
- Python compilation and Bash syntax checks.
- All required R libraries and Python modules load inside the image.
- Coverage statistics match a hand-calculated four-base example, including zero-covered bases and BED/GTF coordinate conversion.
- A BAM fixture verifies exact `NH:i:1` filtering, exclusion of `NH:i:10`, and reverse-stranded coverage.
- Annotation fixtures verify longest-transcript selection, removal of overlapping exons, exclusion of introns overlapping annotated exons, and preservation of opposite-strand features.
- The six-time-point end-to-end test runs GTF processing, STAR indexing, FastQC, Trimmomatic, STAR alignment, samtools validation/indexing, exon/intron HTSeq counting, count merging, preDRUID, DRUID fitting, spike-in fitting, and heatmap generation.
- End-to-end results contain 48 human genes, seven fit columns (standard plus six leave-one-out fits), and 60 introns across the three species. All 48 standard DRUID and spike-in fits are finite.
- Fitting an analytical bounded-growth curve recovers a known three-hour half-life within `1e-4` hours.
- Scaling the six libraries by different factors preserves DRUID half-lives within tolerance `1e-5`.
- The complete current hg38/refGene, dm6/refGene, and sacCer3/sgdGene annotations were merged and processed successfully: 306,488 representative exons, 294,691 non-overlapping exons, and 236,662 filtered introns. This tests the real annotations independently of the unrun full-genome index. See `logs/real-annotations.log` and `reference/validate-real-annotations.py`.
- Both UCSC converters execute on real sacCer3 inputs. The resulting labeled yeast annotation passes `process_GTF.R` and produces nonempty intron output.
- The full-reference command stops with an explicit memory error under the current Docker allocation, before downloading a genome or launching the human index build.

Successful end-to-end outputs are in `work/smoke.1FV5nN/Analysis/HEK293_R1/`. Logs are in `logs/build.log`, `logs/smoke-test.log`, `logs/dockerfile-check.log`, and `logs/memory-guard.log`. Earlier failed test directories remain under `work/` for inspection and are not production analyses.

Final tested image ID:

```text
sha256:93c16c51313f0b81fe05118658ea447168835a9bcb88c1d6ccb4dfabd7ba684f
```

## Key installed versions

| Component | Version |
|---|---|
| DRUID upstream | `455be347cab87b62a2d1f081ec34cafffdf81622`, with documented patches |
| STAR | 2.7.10b |
| samtools | 1.16.1 |
| bedtools | 2.30.0 |
| FastQC | 0.11.9 |
| Trimmomatic | 0.39 |
| Python | 3.11.2 |
| NumPy | 1.24.2 |
| HTSeq | 1.99.2 |
| R | 4.2.2 |
| GenomicFeatures | 1.50.4 |
| rtracklayer | 1.58.0 |
| gplots | 3.1.3 |
| plyr | 1.8.8 |
| SRA Toolkit | 3.0.3 |

The complete package inventory is `/opt/debian-packages.tsv` in the image and `software-versions.tsv` in each completed analysis. Per-analysis workflow provenance includes the upstream commit and hashes of the executed scripts.

## Limits

A complete GSE99517 FASTQ-to-half-life run has **not** been performed. Docker currently has about 12 GB RAM; full indexing and analysis require at least 32 GB. Full compressed FASTQ downloads were also not completed: the slow ENA transfer was stopped, leaving a resumable `RawSequencingData/HEK293_R1/HEK293_R1_01.fastq.gz.partial` file. `druid download` resumes it and verifies its MD5 before using it.

Synthetic execution and numerical checks establish that the workflow connects and executes, but they do not establish agreement with the paper's published half-lives. Modern package versions, the normalization correction, reference annotation changes, and automatic cluster selection can change numerical results. No human genome mapping, biological reproduction, or full-scale performance claim is made.
