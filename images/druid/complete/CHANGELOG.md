# Changelog

## 2026-09-08

- Add GitHub Actions publication to `ghcr.io/yeolab/druid:complete` after end-to-end validation, with rebuilds triggered by supporting-file changes.

- Add an amd64 Dockerfile and Compose service for DRUID's complete-analysis workflow.
- Add verified GEO/ENA mappings and resumable, checksum-verified FASTQ downloads for HEK293 replicate 1.
- Automate combined-reference construction, QC, trimming, alignment, exon/intron quantification, and both half-life analyses.
- Update the GenomicFeatures selection API, port coverage calculation to Python 3, fix exact unique-read filtering, and correct DRUID normalization dimensions while retaining upstream originals.
- Add a synthetic end-to-end test, known-half-life and sequencing-depth-invariance checks, and coverage-statistics checks.
- Document resource requirements, compatibility changes, provenance, and limits of validation.
