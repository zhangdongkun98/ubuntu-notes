ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.0.3-runtime-ubi7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN yum install -y \
    make \
    cuda-command-line-tools-11-0-11.0.3-1 \
    cuda-libraries-devel-11-0-11.0.3-1 \
    cuda-minimal-build-11-0-11.0.3-1 \
    cuda-cudart-devel-11-0-11.0.221-1 \
    cuda-nvprof-11-0-11.0.221-1 \
    cuda-nvml-devel-11-0-11.0.167-1 \
    libcublas-devel-11-0-11.2.0.252-1 \
    libnpp-devel-11-0-11.1.0.245-1 \
    libnccl-devel-2.8.3-1+cuda11.0 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs