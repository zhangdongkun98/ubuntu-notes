ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.2-runtime-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    libcublas-dev=10.2.2.89-1 \
    libnccl-dev=2.8.3-1+cuda10.2 \
    && apt-mark hold libnccl-dev \
    && rm -rf /var/lib/apt/lists/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs