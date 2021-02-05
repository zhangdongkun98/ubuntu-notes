
ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.0.3-runtime-ubuntu16.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-dev-11-0=11.0.221-1 \
    cuda-command-line-tools-11-0=11.0.3-1 \
    cuda-minimal-build-11-0=11.0.3-1 \
    cuda-libraries-dev-11-0=11.0.3-1 \
    cuda-nvml-dev-11-0=11.0.167-1 \
    libnpp-dev-11-0=11.1.0.245-1 \
    libnccl-dev=2.8.3-1+cuda11.0 \
    libcublas-dev-11-0=11.2.0.252-1 \
    libcusparse-11-0=11.1.1.245-1 \
    libcusparse-dev-11-0=11.1.1.245-1 \
    && rm -rf /var/lib/apt/lists/*

# apt from auto upgrading the cublas package. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold libcublas-dev-11-0 libnccl-dev
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs