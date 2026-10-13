# Changelog

## Unreleased

### Fixed

- Pinned LAPA 0.0.5 to pyrle 0.0.38, pyranges 0.0.120, pandas 1.5.3, and
  scipy 1.10.1; `lapa` failed with "Using the coverage method requires that
  pyrle is installed", then on lost strand information and gaussian windows
  with newer versions. The build now checks those code paths.
- Linked `libbz2.so.1` in the SQANTI3 6.0.2 image; its bundled
  `gtfToGenePred` could not load, so `sqanti3_qc.py` failed at "GTF to
  genePred conversion" for every input. The build now runs `gtfToGenePred`.
- Pinned Cerberus 1.1 to pyranges 0.0.127 (with pyrle); pyranges 0.1.4 lost
  strand information in `agg_ends` and `annotate_transcriptome`. Patched
  `replace_gtf_ids` to drop `source` columns that duplicated the GTF source
  field (10-column output, e.g. from TALON GTFs). The build now runs the full
  reference, annotation, and `replace_gtf_ids` workflow.
- Patched Swan 3.2 to draw straight edges with `"arc3"` instead of `None`,
  which current matplotlib rejects; every graph plot failed. The build now
  plots a gene.
- Added the `resource_v1.1.1.txt` resource that the tappAS 1.1.3 application
  expects to its jar (the release ships `resource_v1.1.0.txt`); the first
  start failed with "Unable to extract application resource to files."
- Added `openssh-client` to the Mandalorion 4.6 image; `Mando.py` copies its
  final isoform and quantification files out of `<path>/tmp/` with `scp`,
  so without it the outputs never reached the output directory.
- Patched Isosceles 0.2.1 to call `txdbmaker::makeTxDbFromGFF` (moved out of
  GenomicFeatures in current Bioconductor); `prepare_transcripts()` failed
  without it. The build now runs the bundled bulk RNA-seq example.
- Replaced Debian's minimap2 2.27 package in the FLAIR 3.0.1 image with the
  official minimap2 2.30 release; the Debian build writes `cs:Z` instead of
  `MD:Z` for `--MD`, which made `flair transcriptome` fail with "Missing AS or
  MD tag". The build verification now checks for MD tags.
- Made `suppa.py` on `PATH` in the SUPPA2 2.4 image a wrapper script; upstream
  `suppa.py` has no shebang, so the old symlink failed under `singularity exec`.
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

- rbp-maps v1.1.0 image (`images/rbp-maps/v1.1.0/Dockerfile`), built from the
  upstream release tag with Miniforge and the release's own `environment.yml`;
  publishes `ghcr.io/yeolab/rbp-maps:v1.1.0`.
- Versioned Mandalorion 4.6, ESPRESSO 1.6.0, and Isosceles 0.2.1 containers
  with build-time installation checks and Singularity pull documentation.
- Latest stable containers for the PacBio full-length isoform sequencing
  note's transcript-visualization and isoform-classification/quantification
  tools: Swan 3.2, ggtranscript 1.0.0, SQANTI3 6.0.2, TALON 6.0.1, Cerberus
  1.1, LAPA 0.0.5, FLAIR 3.0.1, lr-kallisto 0.52.0, IsoQuant 4.0.0, Bambu
  3.14.0, and Oarfish 0.10.3. Each image includes a build-time functional
  verification and a versioned GHCR publishing target.
- Latest stable containers for all tools in the PacBio full-length isoform
  sequencing note's differential-analysis sections: tappAS 1.1.3, DESeq2
  1.52.0, DRIMSeq 1.40.0, DEXSeq 1.58.0, and SUPPA2 2.4. Each image includes a
  build-time version and functional smoke test and is published under its
  versioned GHCR tag.
- HOMER 5.1 (`images/homer/5.1`) with bedtools 2.31.1 and Python 3.12 for
  FASTA-mode motif discovery, published as `ghcr.io/yeolab/homer:5.1`.
- skipper-clipper-compare 1.0.0 (`images/skipper-clipper-compare/1.0.0`): the
  pinned Python/bedtools environment for skipper-clipper-snakemake's
  Skipper-vs-CLIPper comparison, published as
  `ghcr.io/yeolab/skipper-clipper-compare:1.0.0`.
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
