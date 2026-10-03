# tappAS 1.1.3

The upstream tappAS 1.1.3 Linux application with R 4.6 and the complete set of
R packages checked by tappAS preinstalled. The vendor application is x86-64
only, so this image is published for `linux/amd64`. Its bundled 8 GB initial
Java heap is reduced to 2 GB for container and CI compatibility; Java may use
up to 75% of the container memory.

tappAS is a desktop GUI and needs access to an X11 display. On a Linux desktop:

```bash
xhost +local:docker
docker run --rm --platform linux/amd64 \
  -e DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$PWD:/work" \
  -v tappas-home:/root \
  ghcr.io/yeolab/tappas:1.1.3
```

The named home volume keeps downloaded annotations, settings, logs, and
projects between runs. Allocate at least 4 CPUs, 6 GB RAM, and 20 GB of free
disk, matching tappAS's own minimum-resource checks.
