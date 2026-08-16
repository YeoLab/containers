# Changelog

## Unreleased

### Fixed

- Updated the ChipSeeker 1.32 image's Jupyter base and fixed the Bioconductor
  data-package post-install hook so its R dependencies install successfully;
  the ChipSeeker package is now pinned to version 1.32.0.
- Fixed first-push Dockerfile detection and removed BuildKit SBOM attachment
  generation, which can exceed GitHub Container Registry's size limit for
  large images; provenance remains enabled.

### Added

- GitHub Actions publishing of changed Dockerfiles to GitHub Container Registry
  (GHCR), including source, SBOM, and provenance metadata.
