#!/bin/bash

set -x
set -e

for test in $(find test/ -iname "*.bats"); do
  if [[ "${test}" == *nvidia-smi* ]] && [[ "${ARCH}" != "x86_64" ]]; then
      # We are running tests on an x86_64 machine for multi-arch and nvidia-smi is passed to the
      # container from the host so it won't work on anything but x86_64.
      echo "Skipping test '${test}' on architecture ${ARCH}"
      continue
  fi
  if [[ "${test}" == *samples* ]] && [[ "${ARCH}" != "x86_64" ]]; then
      # FIXME: Samples tests on multi-arch    
      echo "Skipping test '${test}' on architecture ${ARCH}"
      continue
  fi
  # if [[ "${test}" != "test/01-samples.bats" ]]; then
  #   continue
  # fi
  echo "# Running test script '${test}'"
  /usr/local/bin/bats --tap ${test}
done
