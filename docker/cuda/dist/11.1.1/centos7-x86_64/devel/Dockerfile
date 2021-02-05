ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.1.1-runtime-centos7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN yum install -y \
    make \
    cuda-command-line-tools-11-1-11.1.1-1 \
    cuda-libraries-devel-11-1-11.1.1-1 \
    cuda-minimal-build-11-1-11.1.1-1 \
    cuda-cudart-devel-11-1-11.1.74-1 \
    cuda-nvprof-11-1-11.1.105-1 \
    cuda-nvml-devel-11-1-11.1.74-1 \
    libcublas-devel-11-1-11.3.0.106-1 \
    libnpp-devel-11-1-11.1.2.301-1 \
    libnccl-devel-2.8.3-1+cuda11.1 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs