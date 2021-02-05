#!/usr/bin/env bats

load helpers

image="${IMAGE_NAME}:${CUDA_VERSION}-devel-${OS}${IMAGE_TAG_SUFFIX}"

function setup() {
    docker pull ${image}
    check_runtime
}

@test "check_nvcc_installed" {
    docker_run --rm --gpus 0 ${image} bash -c "stat /usr/local/cuda/bin/nvcc"
    [ "$status" -eq 0 ]
}

@test "check_gcc_installed" {
    docker_run --rm --gpus 0 ${image} bash -c "gcc --version"
    [ "$status" -eq 0 ]
}
