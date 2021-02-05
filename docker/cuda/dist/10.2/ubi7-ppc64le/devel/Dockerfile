ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.2-runtime-ubi7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

RUN yum install -y \
    make \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    libcublas-devel-10.2.2.89-1 \
    cuda-cudart-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    libnccl-devel-2.8.3-1+cuda10.2 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs