ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.1.1-base-ubi8

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN yum install -y \
    cuda-libraries-11-1-11.1.1-1 \
    cuda-nvtx-11-1-11.1.74-1 \
    libnpp-11-1-11.1.2.301-1 \
    libcublas-11-1-11.3.0.106-1 \
    libnccl-2.8.3-1+cuda11.1 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

