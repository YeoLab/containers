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
docker pull --platform linux/amd64 ghcr.io/yeolab/druid:complete
docker run --rm --platform linux/amd64 \
  -v /Volumes/X9Pro/Yeo/DRUID:/work \
  ghcr.io/yeolab/druid:complete druid all
```

Assign at least 32 GB RAM to Docker before running the real-data analysis
(40 GB recommended). The CI test uses a small synthetic reference and does
not download or analyze the full GEO experiment. See the image's
[README](images/druid/complete/README.md) for separate download, reference,
analysis, and fitting commands. The image is also tagged
`ghcr.io/yeolab/druid:sha-<full-commit-sha>`.
