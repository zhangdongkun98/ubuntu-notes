#!/usr/bin/env bats

load helpers

image="${IMAGE_NAME}:${CUDA_VERSION}-devel-${OS}${IMAGE_TAG_SUFFIX}"

function setup() {
    docker pull ${image}
    check_runtime
}

function teardown() {
    cleanup
}

@test "nvidia-smi" {
    docker_run --rm --gpus 0 ${image} nvidia-smi
    [ "$status" -eq 0 ]
}
