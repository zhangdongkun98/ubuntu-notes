ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-runtime-ubuntu14.04
LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
        cuda-nvml-dev-$CUDA_PKG_VERSION \
        cuda-command-line-tools-$CUDA_PKG_VERSION \
cuda-libraries-dev-$CUDA_PKG_VERSION \
        cuda-minimal-build-$CUDA_PKG_VERSION \
        libnccl-dev=$NCCL_VERSION-1+cuda10.1 \
&& \
    rm -rf /var/lib/apt/lists/*

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs