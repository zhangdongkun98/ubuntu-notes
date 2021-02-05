ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.0-base-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.6.4

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-npp-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    cuda-cublas-10-0=10.0.130-1 \
    libnccl2=$NCCL_VERSION-1+cuda10.0 \
    && apt-mark hold libnccl2 \
    && rm -rf /var/lib/apt/lists/*

# apt from auto upgrading the cublas package. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold cuda-cublas-10-0

