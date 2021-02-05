ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.2.0-runtime-centos7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN yum install -y \
    make \
    cuda-command-line-tools-11-2-11.2.0-1 \
    cuda-libraries-devel-11-2-11.2.0-1 \
    cuda-minimal-build-11-2-11.2.0-1 \
    cuda-cudart-devel-11-2-11.2.72-1 \
    cuda-nvprof-11-2-11.2.67-1 \
    cuda-nvml-devel-11-2-11.2.67-1 \
    libcublas-devel-11-2-11.3.1.68-1 \
    libnpp-devel-11-2-11.2.1.68-1 \
    libnccl-devel-2.8.3-1+cuda11.2 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs