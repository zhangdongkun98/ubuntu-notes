ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.2-base-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.4.8

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-npp-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    cuda-cublas-9-2=9.2.148.1-1 \
    libnccl2=$NCCL_VERSION-1+cuda9.2 \
    && apt-mark hold libnccl2 \
    && rm -rf /var/lib/apt/lists/*

