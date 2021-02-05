ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-runtime-centos6

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.7.8

# setopt flag prevents yum from auto upgrading. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN yum install --setopt=obsoletes=0 -y \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    libcublas-devel-10.2.1.243-1 \
    cuda-cudart-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    libnccl-devel-2.7.8-1+cuda10.1 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

RUN yum install -y yum-plugin-versionlock && yum versionlock libcublas10

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs