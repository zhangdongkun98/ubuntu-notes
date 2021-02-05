#!/bin/bash

load /opt/bats/assert/load.bash

dbg() {
  echo "$@" | sed -e 's/^/# /' >&3 ;
}

function cleanup() {
  rm -f Dockerfile
}

function check_runtime() {
    dbg "$(docker info | grep Runtimes)"
    docker info | grep 'Runtimes:' | grep -q 'nvidia'
}

# Taken from runc tests
function docker_run() {
    run docker run "$@"
    echo "docker run $@ (status=$status):" >&2
    echo "$output" >&2
}

function docker_build() {
    run docker build --pull "$@"
    echo "docker run $@ (status=$status):" >&2
    echo "$output" >&2
}

function nvidia_container_runtime_run() {
    run nvidia-container-runtime run "$@"

    echo "nvidia-container-runtime run $@ (status=$status):" >&2
    echo "$output" >&2
}

function run_nvidia_smi() {
    local image=$1
    docker pull $image >/dev/null 2>&1 || true
    docker_run --rm --gpus all -e NVIDIA_VISIBLE_DEVICES=all $image nvidia-smi
    [ "$status" -eq 0 ]
}

function skip_if_userns() {
    run sh -c "docker info -f  '{{ .SecurityOptions }}' | grep -q userns"
    if [[ "$status" -eq 0 ]]; then
        skip "user NS enabled."
    fi
}

function skip_if_nouserns() {
    run sh -c "docker info -f  '{{ .SecurityOptions }}' | grep -q userns"
    if [[ "$status" -eq 1 ]]; then
        skip "user NS not enabled."
    fi
}

function skip_if_headless() {
    run pidof X Xorg
    if [[ "$status" -eq 1 ]]; then
        skip "no X server is running"
    fi
}

function skip_if_nonroot() {
    if [[ "$(id -u)" -ne 0 ]]; then
        skip "running as non-root"
    fi
}

function skip_if_ngc_cli_not_installed() {
    run sh -c "which ngc"
    if [[ "$status" -eq 1 ]]; then
        skip "ngc cli is not installed."
    fi
}

function debug() {
    if [ $DEBUG -eq 1 ]; then
        echo "$@" | sed -e 's/^/# /' >&3 ;
    fi
}
