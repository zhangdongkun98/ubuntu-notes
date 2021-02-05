ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.2-base-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-npp-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    libcublas10=10.2.2.89-1 \
    libnccl2=$NCCL_VERSION-1+cuda10.2 \
    && apt-mark hold libnccl2 \
    && rm -rf /var/lib/apt/lists/*

