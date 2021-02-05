ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.1-devel-ubuntu16.04
LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV CUDNN_VERSION 7.1.3.16

LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    libcudnn7=$CUDNN_VERSION-1+cuda9.1 \
    libcudnn7-dev=$CUDNN_VERSION-1+cuda9.1 \
    && apt-mark hold libcudnn7 && \
    rm -rf /var/lib/apt/lists/*
