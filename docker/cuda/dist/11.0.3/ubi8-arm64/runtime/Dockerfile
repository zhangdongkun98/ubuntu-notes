ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.0.3-base-ubi8

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN yum install -y \
    cuda-libraries-11-0-11.0.3-1 \
    cuda-nvtx-11-0-11.0.167-1 \
    libnpp-11-0-11.1.0.245-1 \
    libcublas-11-0-11.2.0.252-1 \
    libnccl-2.8.3-1+cuda11.0 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

