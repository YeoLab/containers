# docker-images

Collection of Dockerfiles and a GitHub Actions publishing workflow.

## Publishing to GHCR

Pushing a new or changed file named `Dockerfile` starts the **Publish changed
Dockerfiles to GHCR** workflow. It builds the Dockerfile using its containing
directory as the build context and publishes the result to GitHub Container
Registry (GHCR).

For the repository's standard layout, use:

```text
images/<image-name>/<version>/Dockerfile
```

For example, a change to `images/fastp/0.23.3/Dockerfile` publishes:

```text
ghcr.io/yeolab/fastp:0.23.3
ghcr.io/yeolab/fastp:sha-<full-commit-sha>
```

The version tag is convenient for normal use; the SHA tag identifies the exact
source revision used to build it. For a strictly immutable reference, record
and pull the image digest shown in GHCR. A Dockerfile directly under
`images/<image-name>/` receives the `latest` tag. For a Dockerfile outside
`images/`, the workflow derives a lowercase image name from its directory and
uses the `latest` tag, so new locations do not require an edit to the workflow.

Images include OCI source and revision labels plus BuildKit provenance and an
SBOM. GitHub associates the resulting package with this repository; package
visibility, access permissions, retention, and version deletion can be managed
from the repository's **Packages** page.

You can also run the workflow manually from the **Actions** page and provide
one Dockerfile path; this is useful for rebuilding a single image without
changing its source.

The workflow uses the repository-scoped `GITHUB_TOKEN` and needs `packages:
write`, already declared in the workflow. If organization policy prevents a
publish, allow GitHub Actions to create packages for this repository or replace
the token with an approved package-write token.

## PacBio full-length isoform analysis

The tools listed under **Differential transcript analysis** and **Differential
splicing usage** in PacBio's full-length isoform sequencing application note
are available as individually versioned images:

| Application-note section | Tool | Image |
| --- | --- | --- |
| Differential transcript analysis | tappAS 1.1.3 | `ghcr.io/yeolab/tappas:1.1.3` |
| Differential transcript analysis | DESeq2 1.52.0 | `ghcr.io/yeolab/deseq2:1.52.0` |
| Differential transcript analysis | DRIMSeq 1.40.0 | `ghcr.io/yeolab/drimseq:1.40.0` |
| Differential splicing usage | DEXSeq 1.58.0 | `ghcr.io/yeolab/dexseq:1.58.0` |
| Differential splicing usage | SUPPA2 2.4 | `ghcr.io/yeolab/suppa2:2.4` |

DESeq2, DRIMSeq, and DEXSeq use the Bioconductor 3.23 release on R 4.6.
SUPPA2 is a command-line image whose arguments are passed directly to
`suppa.py`. tappAS is an x86-64 GUI image and needs an X11 display; see each
image directory's README for launch examples and resource requirements. Every
Dockerfile contains a build-time smoke test, so GitHub Actions publishes an
image only after its installed version and a representative operation pass.

The application note's transcript-visualization tools are also available:

| Application-note section | Tool | Image |
| --- | --- | --- |
| Transcript visualization | Swan 3.2 | `ghcr.io/yeolab/swan:3.2` |
| Transcript visualization | ggtranscript 1.0.0 | `ghcr.io/yeolab/ggtranscript:1.0.0` |

The latest stable releases of the note's isoform classification and
quantification tools are packaged as:

| Tool | Image |
| --- | --- |
| SQANTI3 6.0.2 | `ghcr.io/yeolab/sqanti3:6.0.2` |
| TALON 6.0.1 | `ghcr.io/yeolab/talon:6.0.1` |
| Cerberus 1.1 | `ghcr.io/yeolab/cerberus:1.1` |
| LAPA 0.0.5 | `ghcr.io/yeolab/lapa:0.0.5` |
| FLAIR 3.0.1 | `ghcr.io/yeolab/flair:3.0.1` |
| lr-kallisto / kallisto LongKmer 0.52.0 | `ghcr.io/yeolab/lr-kallisto:0.52.0` |
| IsoQuant 4.0.0 | `ghcr.io/yeolab/isoquant:4.0.0` |
| Bambu 3.14.0 | `ghcr.io/yeolab/bambu:3.14.0` |
| Oarfish 0.10.3 | `ghcr.io/yeolab/oarfish:0.10.3` |

Swan and the Python command-line tools use checksum-pinned release artifacts;
ggtranscript is pinned to the current upstream commit because the project has
not published GitHub releases. SQANTI3 and TALON use exact Bioconda builds,
Bambu uses Bioconductor 3.23, and lr-kallisto uses kallisto's official
LongKmer binary. The per-image READMEs document entrypoints, architecture, and
upstream version caveats. Build-time tests exercise transcript parsing,
annotation conversion, database creation, indexing, or quantification as
appropriate instead of checking only `--version` output.

## Pulling a Singularity/Apptainer image from GHCR

Install [Apptainer](https://apptainer.org/) (or SingularityCE), then pull a
published image directly from GHCR:

```bash
apptainer pull fastp_0.23.3.sif docker://ghcr.io/yeolab/fastp:0.23.3
```

For a strictly reproducible pull, replace the tag with the digest displayed on
the GHCR package version:

```bash
apptainer pull fastp.sif docker://ghcr.io/yeolab/fastp@sha256:<image-digest>
```

For a private GHCR package, authenticate before pulling. With Apptainer, use a
GitHub classic personal access token that has `read:packages` access:

```bash
export CR_PAT=ghp_your_token
printf '%s' "$CR_PAT" | apptainer registry login --username YOUR_GITHUB_USER --password-stdin docker://ghcr.io
apptainer pull fastp_0.23.3.sif docker://ghcr.io/yeolab/fastp:sha-<full-commit-sha>
```

Set the GHCR package to public from GitHub's **Packages** page if users should
be able to pull it without credentials.

## DRUID complete analysis

The [DRUID build context](images/druid/complete/) includes the software,
GEO/ENA sample manifest, full-analysis runner, and synthetic end-to-end tests.
Changes to any file in `images/druid/complete/` trigger publishing, including
changes to scripts, tests, and configuration. The publishing workflow itself
also triggers a DRUID rebuild. CI builds for `linux/amd64`, runs the complete
synthetic analysis and reference-converter checks, and publishes only after
those checks pass. Validation logs, half-life tables, heatmaps, and provenance
are retained as Actions artifacts for 14 days.

```bash
singularity pull druid.sif docker://ghcr.io/yeolab/druid:sha-7941ba6aebf0fd4beb48643ec373374b50b02bbc
export DRUID_IMAGE="$PWD/druid.sif"
mkdir -p "$HOME/DRUID/tmp" "$HOME/DRUID/logs"
cd "$HOME/DRUID"
singularity exec --cleanenv --env THREADS=8,TMPDIR=/work/tmp \
  --bind "$PWD:/work" --pwd /work "$DRUID_IMAGE" druid all \
  2>&1 | tee logs/full-analysis.log
```

Run on an x86-64 cluster compute node with at least 32 GB RAM (40 GB
recommended) and eight CPUs. The CI test uses a small synthetic reference and
does not download or analyze the full GEO experiment. See the image's
[README](images/druid/complete/README.md) for scheduler guidance and separate
download, reference, analysis, and fitting commands. The image is also tagged
`ghcr.io/yeolab/druid:sha-<full-commit-sha>`.
