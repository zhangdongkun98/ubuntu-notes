# Nvidia CUDA Linux Container Image Sources

Usage of the CUDA container images requires the [Nvidia Container Runtime](https://github.com/NVIDIA/nvidia-container-runtime).

Container images are available from:

- https://ngc.nvidia.com/catalog/containers/nvidia:cuda
- https://hub.docker.com/r/nvidia/cuda

## Announcement

The "latest" tag for CUDA, CUDAGL, and OPENGL images has been deprecated on NGC and Docker Hub.

With the removal of the latest tag, the following use case will result in the "manifest unknown"
error:

```
$ docker pull nvidia/cuda
Error response from daemon: manifest for nvidia/cuda:latest not found: manifest unknown: manifest
unknown
```

This is not a bug.

## IMAGE SECURITY NOTICE

The CUDA images are scanned for CVE vulnerabilities prior to release and some images may contain CVEs at the time of publication.

Our Product Security teams reviews the CVEs and determines if the CVE should block the release or not. We try to mitigate as much as we can, but since we do not control the upstream base images, some cuda image releases might be impacted.

Please consult the README on the NGC or Docker Hub pages for details.

## LD_LIBRARY_PATH NOTICE

The `LD_LIBRARY_PATH` is set inside the container to legacy nvidia-docker v1 paths that do not exist on newer installations. This is done to maintain compatibility for our partners that still use nvidia-docker v1 and this will not be changed for the forseable future. [There is a chance this might cause issues for some.](https://gitlab.com/nvidia/container-images/cuda/-/issues/47)

## Building from source

The container image scripts are archived in the `dist/` directory and are available for all supported distros and cuda versions.

Here is an example on how to build an image set for ubuntu20.04 and CUDA 11.0,

```bash
#/bin/bash

export IMAGE_NAME="nvidia/cuda"
export CUDA_VERSION="11.0"
export OS="ubuntu20.04"
export ARCH=`uname -m`

docker build -t "${IMAGE_NAME}:${CUDA_VERSION}-base-${OS}" "dist/${CUDA_VERSION}/${OS}-${ARCH}/base"
docker build -t "${IMAGE_NAME}:${CUDA_VERSION}-runtime-${OS}" --build-arg "IMAGE_NAME=${IMAGE_NAME}" "dist/${CUDA_VERSION}/${OS}-${ARCH}/runtime"
docker build -t "${IMAGE_NAME}:${CUDA_VERSION}-devel-${OS}" --build-arg "IMAGE_NAME=${IMAGE_NAME}" "dist/${CUDA_VERSION}/${OS}-${ARCH}/devel"
```

## Cuda Container Image Automation

The [dev.md](https://gitlab.com/nvidia/container-images/cuda/blob/master/doc/dev.md) document provides details on how the gitlab pipelines work and how to control, modify, or debug them.





# Other
```bash
git clone https://gitlab.com/nvidia/container-images/cuda.git
```