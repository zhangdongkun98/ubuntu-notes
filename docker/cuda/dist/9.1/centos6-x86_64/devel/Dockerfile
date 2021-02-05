ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.1-runtime-centos6

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

RUN yum install -y \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    libcublas-devel- \
    cuda-cudart-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    && yum clean all \
    && rm -rf /var/cache/yum/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs