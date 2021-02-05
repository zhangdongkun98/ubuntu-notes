# Scripts for testing CUDA Docker

## Requirements

### Bash Automated Test System

https://github.com/bats-core/bats-core

See install script (mentioned below).

## Globals

Globals that are used by the tests scripts.

* `REGISTRY`: The docker image registry to use in the image names.

   Default is unset which the docker command resolves to hub.docker.com automatically when pushing
   or pulling.

* `REGISTRY_USER`: The user to login to the docker registry as.

   Default is nvcr.io

* `IMAGE_TAG`: The tag of the image being tested.

## Usage

### Setup

```sh
sudo test/scripts/bats_install.sh
```

### Usage

```sh
sudo test/scripts/run_tests.sh
```
