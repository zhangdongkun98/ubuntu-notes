ARG IMAGE_NAME
FROM ${IMAGE_NAME}:8.0-devel-ubi7
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 5.1.10
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=c10719b36f2dd6e9ddc63e3189affaa1a94d7d027e63b71c3f64d449ab0645ce && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v5.1/cudnn-8.0-linux-x64-v5.1.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-8.0-linux-x64-v5.1.tgz" | sha256sum -c - && \
    gunzip cudnn-8.0-linux-x64-v5.1.tgz && \
    tar --no-same-owner -xf cudnn-8.0-linux-x64-v5.1.tar -C /usr/local && \
    rm cudnn-8.0-linux-x64-v5.1.tar && \
    ldconfig
