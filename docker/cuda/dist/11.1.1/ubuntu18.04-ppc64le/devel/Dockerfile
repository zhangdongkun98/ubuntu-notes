
ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.1.1-runtime-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-dev-11-1=11.1.74-1 \
    cuda-command-line-tools-11-1=11.1.1-1 \
    cuda-minimal-build-11-1=11.1.1-1 \
    cuda-libraries-dev-11-1=11.1.1-1 \
    cuda-nvml-dev-11-1=11.1.74-1 \
    libnpp-dev-11-1=11.1.2.301-1 \
    libnccl-dev=2.8.3-1+cuda11.1 \
    libcublas-dev-11-1=11.3.0.106-1 \
    libcusparse-11-1=11.3.0.10-1 \
    libcusparse-dev-11-1=11.3.0.10-1 \
    && rm -rf /var/lib/apt/lists/*

# apt from auto upgrading the cublas package. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold libcublas-dev-11-1 libnccl-dev
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs