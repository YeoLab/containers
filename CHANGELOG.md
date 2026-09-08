# Changelog

## Unreleased

### Fixed

- Run DRUID CI validation with the GitHub Actions runner's UID/GID so its
  root-owned smoke-test directory no longer prevents artifact upload after a
  successful image publication.
- Pinned the Bento Tools 2.1.3 base image to RAPIDS Singlecell 0.10.9 so its
  legacy CUDA 12.6 dependency set is not broken by changes to the `latest` tag.
- Updated the Bento Tools 2.1.3 image to cryptography 49.0.0 and its required
  cffi 2.0.0 dependency to remediate CVE-2026-69249 (GHSA-jwv3-5hgf-82ww).
- Updated the ChipSeeker 1.32 image's Jupyter base and fixed the Bioconductor
  data-package post-install hook so its R dependencies install successfully;
  the ChipSeeker package is now pinned to version 1.32.0.
- Fixed first-push Dockerfile detection and removed BuildKit SBOM attachment
  generation, which can exceed GitHub Container Registry's size limit for
  large images; provenance remains enabled.

### Added

- Singularity-first DRUID deployment and tutorial instructions for Dockerless
  clusters, including the tested `sha-7941ba6aebf0fd4beb48643ec373374b50b02bbc`
  image pull command.
- DRUID complete-analysis container at `images/druid/complete`, including
  verified GEO/ENA sample mappings, compatibility fixes, and full workflow tests.
- DRUID builds triggered by supporting-file changes; GitHub Actions tests the
  container before publishing `ghcr.io/yeolab/druid:complete` and a commit tag,
  and retains validation artifacts for 14 days.

- GitHub Actions publishing of changed Dockerfiles to GitHub Container Registry
  (GHCR), including source, SBOM, and provenance metadata.
