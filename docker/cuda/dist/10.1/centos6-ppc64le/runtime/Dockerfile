ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-base-centos6

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.7.8

RUN yum install -y \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    cuda-npp-$CUDA_PKG_VERSION \
    libcublas10-10.2.1.243-1 \
    libnccl-2.7.8-1+cuda10.1 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

