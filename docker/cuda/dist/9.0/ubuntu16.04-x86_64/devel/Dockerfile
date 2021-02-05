ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.0-runtime-ubuntu16.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-core-9-0=9.0.176.3-1 \
    cuda-cublas-dev-9-0=9.0.176.4-1 \
    && rm -rf /var/lib/apt/lists/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs