ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.0-runtime-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.6.4

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-cublas-dev-10-0=10.0.130-1 \
    libnccl-dev=2.6.4-1+cuda10.0 \
    && apt-mark hold libnccl-dev \
    && rm -rf /var/lib/apt/lists/*

# apt from auto upgrading the cublas package. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold cuda-cublas-dev-10-0

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs