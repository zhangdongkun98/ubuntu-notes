ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.2-base-centos6

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.4

RUN yum install -y \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    libnccl-2.4.8+cuda9.2 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

