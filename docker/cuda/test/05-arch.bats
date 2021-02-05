#!/usr/bin/env bats

load helpers

image="${IMAGE_NAME}:${CUDA_VERSION}-devel-${OS}${IMAGE_TAG_SUFFIX}"

function setup() {
    check_runtime
}

@test "check_architecture" {
    narch=${ARCH}
    if [[ ${ARCH} == "arm64" ]]; then
        narch="aarch64"
    fi
    docker pull ${image}
    docker_run --rm --gpus 0 ${image} bash -c "[[ \$(uname -m) == ${narch} ]] || false"
    [ "$status" -eq 0 ]
}
