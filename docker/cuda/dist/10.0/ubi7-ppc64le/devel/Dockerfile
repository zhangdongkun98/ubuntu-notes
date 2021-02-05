ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.0-runtime-ubi7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.6.4

# setopt flag prevents yum from auto upgrading. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN yum install --setopt=obsoletes=0 -y \
    make \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    cuda-cublas-dev-$CUDA_PKG_VERSION \
    cuda-cudart-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    libnccl-devel-2.6.4-1+cuda10.0 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs