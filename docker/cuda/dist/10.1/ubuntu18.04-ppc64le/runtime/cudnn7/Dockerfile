ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-runtime-ubuntu18.04
LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

ENV CUDNN_VERSION 7.6.5.32

LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN apt-get update && apt-get install -y --no-install-recommends \
    libcudnn7=$CUDNN_VERSION-1+cuda10.1 \
    && apt-mark hold libcudnn7 && \
    rm -rf /var/lib/apt/lists/*
