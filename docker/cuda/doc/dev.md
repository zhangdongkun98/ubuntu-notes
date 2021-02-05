# Cuda Container Pipeline Automation Documentation

This document is divided into three sections:

1. [Development Environment](#development-environment): Setup the Python environment for developing the automation script.
1. [Gitlab Pipelines](#gitlab-pipelines): Contains details on how to operate the gitlab automation.
1. [Image Manifests](#image-manifests): Features of the yaml file used to generate image scripts.
1. [Implementation](#implementation): Clues as to how manager.py is implemented
1. [Use cases and Troubleshooting](#use-cases-and-troubleshooting): How to do a thing or fix a problem quickly.

## Development Environment

Setup the environment to work on manager.py and generate container image scripts from templates for building images.

### Setup

1. Install poetry. See https://poetry.eustace.io/docs/#installation

1. Install the dependencies with `poetry install`

1. Enter the virtual environment with `poetry shell`

Once in the virtual environment, run the script with:

```
python manager.py
```

# Gitlab Pipelines

## Triggering pipelines

Pipelines can be triggered automatically or explicitly via commit message.

The CUDA pipelines use the "Directed Acyclic Graph" (dag) feature of Gitlab to allow stages to run concurrently and independently.

### Manual triggering with optional dry-run

To run the pipelines without pushing a commit,

1. Go to the [pipelines](https://gitlab-master.nvidia.com/cuda-installer/cuda/pipelines) page and click "Run Pipeline".

1. Ensure the correct branch of the repo is selected.

1. Add an input variable, it should be set to `TRIGGER_OVERRIDE` with a value of "all", or...

   1. A set of distros, or cuda versions. The "Explicit Triggering" section below has details on the potential of this value.

1. Add an input variable, it should be set to `DRY_RUN` with a value of "1".

   1. This will run the pipelines without publishing to the configured container repositories.

1. Click "Run Pipeline"

### Automatic triggering

FIXME: As of June 17, 2020 this feature is broken. It will be fixed at a future date or removed.

By default on the master branch, the manifest.yaml file is compared against the previous version from the last commit. The changed keys within the manifest are then used to trigger builds via the gitlab api.

### Explicit triggering

Pipeline triggering can be overridden via the git commit message or the `TRIGGER_OVERRIDE` variable with:

```
ci.trigger = <pipeline>[,...]
```

Where pipeline can be:

- `all`: All of the pipelines are built.
- `cuda<major>.<minor>`: A cuda version for all distros.
- `cuda<major>.<minor>-<arch>`: A cuda version for an architecture.
- `<distro>`: all cuda versions for a distro.
- `<distro>-<arch>`: all cuda versions for a distro for a particular architecture
- `<distro><distro_version>`: all cuda versions for a distro version.
- `<distro><distro_version>-<arch>`: all cuda versions for a distro version for a particular architecture
- `cuda<major>.<minor>-<distro><distro_version>`: A specific cuda version and distro for all architectures
- `cuda<major>.<minor>-<distro><distro_version>-<arch>`: A very specify cuda version, distro, and arch.
- `name:<pipeline_name>`: A named pipeline. See [Named image pipelines](#named-image-pipelines)
- **TODO**: `cudnn<version>`: A cudnn version for all distros.

### Examples

* `ci.trigger = cuda11.0`: All cuda 11.0 pipelines for all platforms and architectures.
* `ci.trigger = ubuntu18.04-cuda11.0`: All ubuntu18.04 pipelines for cuda11.0 on all supported architectures.
* `ci.trigger = ubuntu18.04,ubuntu16.04`: All ubuntu18.04 and 16.04 pipelines for all supported cuda versions and architectures.
* `ci.trigger = ubuntu18.04-cuda11.0-x86_64`: Only ubuntu18.04 cuda11.0 pipeline for x86_64.

# Image Manifests

Configuration of Dockerfile and Test output for the numerous platforms and architectures supported by CUDA Docker is defined in a manifest yaml. [cuda.yaml](https://gitlab.com/nvidia/container-images/cuda/blob/master/manifests/cuda.yaml) contains the latest examples of supported features.

The manifest is also used to generate gitlab pipelines.

### Image definition

To define a new image and pipeline:

```
.components_v11.0: &cuda11_0_components
  build_version: 194
  # ... truncated
  libnccl2:
    version: 2.7.8-1
  libnccl2_dev:
    version: 2.7.8-1
  cudnn8:
    version: 8.0.2.39-1

cuda_v11.0:
  dist_base_path: dist/11.0
  image_name: nvidia/cuda
  ubuntu18.04:
    template_path: templates/ubuntu
    skip_tests: True
    image_tag_suffix: "-rc"
    # base_image defined at this level will indicate the image manifest supports multi-arch
    base_image: ubuntu:18.04
    push_repos:
      - artifactory
      - docker.io
      - nvcr.io
    x86_64:
      latest: True
      no_os_suffix: True
      <<: *cuda11_0_requires
      components:
        # Component versions can be shared across architectures and overidden where they differ
        # this is a feature of yaml called "Merge Key Language-Independent Type" https://yaml.org/type/merge.html
        <<: *cuda11_0_components
        cudnn8:
          version: 8.0.0.180
          sha256sum: 68558bfa5d1dd6d0300dacaea6ad66ed516ea7dfea01343bd552e6efa107b44c
          source: https://developer.download.nvidia.com/compute/redist/cudnn/v8.0.0/Ubuntu18_04-x64/libcudnn8_8.0.0.180-1+cuda11.0_amd64.deb
          dev:
            sha256sum: 8d5430c00d698c2695f4025a0a07975beaecd6c37c8c494acac112977776e332
            source: https://developer.download.nvidia.com/compute/redist/cudnn/v8.0.0/Ubuntu18_04-x64/libcudnn8-dev_8.0.0.180-1+cuda11.0_amd64.deb
        libnccl2:
          version: 2.7.3
          sha256sum: d112b722bf557cff96d571ac3386e4f539be7b3e9412561bde59b0ad6e59263d
          source: https://developer.download.nvidia.com/compute/redist/nccl/v2.7/nccl_2.7.3-1+cuda11.0_x86_64.txz
    ppc64le:
      # Re-defining base_image at this level will force the ppc64le templates to use this base_image
      # instead of the multi-arch ubuntu18.04 base image
      # base_image: ppc64le/ubuntu:18.04
      exclude_repos:
        - nvcr.io
    arm64:
      components:
        <<: *cuda11_0_components
        # cudnn8 is unset because it does not exist for arm64
        # It is still set, but we empty it because yaml doesn't give a better way to do this. The
        # templates will check the value.
        cudnn8:
```

A pipeline definition will allow the creation of container image scripts and gitlab pipelines to build, test, scan, and ship CUDA images for all supported platforms and architectures.

The pipeline definition will cuda image generation, build, test, and scanning stages.

`cuda_v11.0` is the cuda version for the pipeline. It can contain an optional name: [Named image pipelines](#named-image-pipelines).

Keys:

* `dist_base_path`: The path from which the container image scripts will be saved to and read from.
* `image_name`: The image name to generate when building the container images in this pipeline.
* `template_path`: The path to search in for templates for this image. The path should be relative to manager.py.
* `skip_tests`: Optional boolean - Don't generate tests for the cuda version.
* `image_tag_suffix`: Optional string - The image name will have this value appended to them.
* `base_image`: The image to base the cuda images off of. By default, multi-arch base images should be used.
* `push_repos`: The repos to push the images to. See [Container Repositories](#container-repositories).
* `exclude_repos`: The repos to push the images to. See [Container Repositories](#container-repositories).
* `components`: Is a list of cuda components to install in the distro. See [CUDA Component Selection](#cuda-component-selection).
  * `source`: The component will be fetched from source and verified to match sha256sum. Will also need to be sepecified for the `dev` components.
  * `sha256sum`: Used to verify the fetched component. Can be used without `source` for centos cudnn
                 components.

The [Implementation](#implementation) section contains clues on how manager.py is implemented.

#### Generating image scripts from the manifest

Everything:

```
python manager.py generate --all                                        # Everything
```

Targeted:

```
python manager.py generate --os ubi --os-version 7 --cuda-version 10.1  # A specific target
```

### Cuda Component Selection

TODO

### Named image pipelines

Special pipelines can be created by appending `_<name>` to the end of the cuda image definition.

```yaml
push_repos:
  # TODO: allow merging named pipeline push repos so we don't duplicate too much
  artifactory_l4t:
    only_if: NV_ARTIFACTORY
    user: ARTIFACTORY_USER
    pass: ARTIFACTORY_PASS
    registry:
      arm64: urm.nvidia.com/sw-gpu-cuda-installer-docker-local/cuda/l4t-cuda

cuda_v11.0_l4t:
  dist_base_path: dist/10.2/l4t
  image_name: nvidia/l4t-cuda
  artifactory:
    - artifactory_l4t
  ubuntu18.04:
    template_path: templates/ubuntu
    skip_tests: True
    push_repos:
      - artifactory_l45
    arm64:
      base_image: nvcr.io/nvidia/l4t-base:r32.4.2
```

Named image pipelines can be defined by specifying a new section in the manifest with the name as the suffix.

where:

* `version`: The cuda version.
* `flavor`: The name of this flavor of the cuda images. No special characters in the name are allowed!
* `base_image`: The base image to build the cuda images off of.
* `image_name`: The name of the images that will be pushed to the configured repositories.
* `push_repos`: The repo to push to. This requires defining a new push repo with the explicit details for the pipeline.

### Container Repositories

It is possible to define multiple repositories to push images to, and select / unselect repositories for a
specific distro or architecture.

```yaml
push_repos:
  # Staging
  artifactory:
    only_if: NV_ARTIFACTORY
    user: ARTIFACTORY_USER
    pass: ARTIFACTORY_PASS
    registry:
      x86_64: urm.nvidia.com/sw-gpu-cuda-installer-docker-local/cuda
      ppc64le: urm.nvidia.com/sw-gpu-cuda-installer-docker-local/cuda/cuda-ppc64le
      arm64: urm.nvidia.com/sw-gpu-cuda-installer-docker-local/cuda/cuda-arm64
```

`push_repos` accepts an arbitrary number of key:value pairs of potential image repositories.

* `artifactory`: The name of the push repo for reference.
* `only_if`: If this key is set, then the repo will only be used if the value of this variable is set in the environment. Used for gitlab ci internal / public.
* `user/pass`: The user and password to login to the image repository with.
* `registry` can contain only three subkeys: `x86_64`, `ppc64le`, and `arm64`.
  * For each of the subkeys, the values must be the image name to be set for the images.

#### Repo selection

Every distro must have configured `push_repos`:

```yaml
cuda_v11.0:
  dist_base_path: dist/11.0
  ubuntu18.04:
    template_path: templates/ubuntu
    image_tag_suffix: "-rc"
    push_repos:
      - artifactory
      - docker.io
      - nvcr.io
    arm64:
      base_image: arm64v8/ubuntu:18.04
      exclude_repos:
        - nvcr.io
```

* `push_repos`: Is an array of image repositories defined in document level `push_repos`.
* `exclude_repos`: Is an array of image names from the document level `push_repos`. The repos will not have images pushed to them on deploy.

# Implementation details

The output process for the `generate` command:

1. manifest.yaml is read.
1. `.gitlab-ci.yml` is generated from templates.
1. The gitlab pipeline yaml file is used to generate images from templates.

This process should be redone to decouple generating images verses generating pipelines, but for now
if there is an error in the gitlab pipeline generated from templates, the cuda image scripts will
  fail to generate.

# Use cases and Troubleshooting

Common use cases and troubleshooting.

## Add a new pipeline

TODO

## Running pipelines without deployment

It is useful to see what would be pushed to where upon a successful pipeline. When `DRY_RUN` is
used, the deployment stage will show what tags would be created and what repositories they would be
pushed to without the pushing.

1. Use `[ ci skip ]` in the commit message. Doc: [Skip running pipelines on a commit](#skip-running-pipelines-on-a-commit).
1. Manually trigger the pipeline using the `DRY_RUN=1` variable. Doc: [Manual triggering with optional dry-run](#manual-triggering-with-optional-dry-run).

### Testing deployment locally

The [Development Environment](#development-environment) section details how to setup the python
environment to run `manage.py`.

```
export NV_ARTIFACTORY=1
export ARTIFACTORY_USER="svc-compute-packagin"
export ARTIFACTORY_PASS="password"
export ARCH=arm64
export OS=ubuntu18.04
export IMAGE_NAME=nvidia/l4t-cuda
export OS_NAME=ubuntu
export OS_VERSION=18.04
export CUDA_VERSION=10.2
export CUDNN_VERSION=
export PIPELINE_NAME=l4t

python manager.py --manifest manifests/cuda.yaml push --image-name "${IMAGE_NAME}" --os "${OS_NAME}" --os-version "${OS_VERSION}" --cuda-version "${CUDA_VERSION}" --arch "${ARCH}" --pipeline-name "${PIPELINE_NAME}" -n
```

The `-n` here is crucial to not push.

## Skip running pipelines on a commit

In the description of the commit message, use:

```
[ci skip]
```

This is a feature of the Gitlab CI tool.
