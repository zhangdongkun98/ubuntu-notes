ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.2.0-base-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-libraries-11-2=11.2.0-1 \
    libnpp-11-2=11.2.1.68-1 \
    cuda-nvtx-11-2=11.2.67-1 \
    libcublas-11-2=11.3.1.68-1 \
    libnccl2=$NCCL_VERSION-1+cuda11.2 \
    && rm -rf /var/lib/apt/lists/*

# apt from auto upgrading the cublas package. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold libcublas-11-2 libnccl2
