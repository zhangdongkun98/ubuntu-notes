ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.1-base-ubuntu16.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-npp-$CUDA_PKG_VERSION \
    cuda-cublas-9-1=9.1.85.3-1 \
    && rm -rf /var/lib/apt/lists/*

