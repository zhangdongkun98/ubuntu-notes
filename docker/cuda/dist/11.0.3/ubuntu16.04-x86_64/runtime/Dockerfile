ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.0.3-base-ubuntu16.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-11-0=11.0.3-1 \
    libnpp-11-0=11.1.0.245-1 \
    cuda-nvtx-11-0=11.0.167-1 \
    libcublas-11-0=11.2.0.252-1 \
    libnccl2=$NCCL_VERSION-1+cuda11.0 \
    && rm -rf /var/lib/apt/lists/*

# apt from auto upgrading the cublas package. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold libcublas-11-0 libnccl2
