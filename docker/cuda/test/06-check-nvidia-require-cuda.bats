#!/usr/bin/env bats

load helpers

image="${IMAGE_NAME}:${CUDA_VERSION}-devel-${OS}${IMAGE_TAG_SUFFIX}"

function setup() {
    docker pull ${image}
    check_runtime
}

@test "check_LD_LIBRARY_PATH" {
    # The devel images for x86_64 should always contain "brand=tesla"
    docker_run --rm --gpus 0 ${image} bash -c "printenv | grep -q 'brand=tesla'"
    [ "$status" -eq 0 ]
}
