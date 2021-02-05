ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.2-runtime-centos7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.4.8

RUN yum install -y \
    make \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    cuda-cublas-dev-$CUDA_PKG_VERSION \
    cuda-cudart-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    libnccl-devel-2.4.8+cuda9.2 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs