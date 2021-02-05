ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.2-base-ubuntu16.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-npp-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    cuda-cublas-9-2=9.2.148.1-1 \
    && rm -rf /var/lib/apt/lists/*

