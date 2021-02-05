ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.0-base-ubi7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.6.4

# setopt flag prevents yum from auto upgrading. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN yum install --setopt=obsoletes=0 -y \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-cublas-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    libnccl-2.6.4-1+cuda10.0 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

