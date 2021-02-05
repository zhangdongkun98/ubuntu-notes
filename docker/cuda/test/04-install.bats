#!/usr/bin/env bats

load helpers

image="${IMAGE_NAME}:${CUDA_VERSION}-devel-${OS}${IMAGE_TAG_SUFFIX}"

function setup() {
    check_runtime
}

@test "check_multiple_cuda_directories" {
    # There can be only one...
    # If a wrong dependency version is selected for a different cuda version, it will pull in other packages and install to a
    # different cuda version. We only want one cuda version in the images
    docker pull ${image}
    docker_run --rm --gpus 0 ${image} bash -c "[[ \$(ls -l /usr/local/ | grep cuda | wc -l) == 2 ]] || false"
    [ "$status" -eq 0 ]
}
