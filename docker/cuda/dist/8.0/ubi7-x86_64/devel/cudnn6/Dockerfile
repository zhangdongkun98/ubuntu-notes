ARG IMAGE_NAME
FROM ${IMAGE_NAME}:8.0-devel-ubi7
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 6.0.21
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=9b09110af48c9a4d7b6344eb4b3e344daa84987ed6177d5c44319732f3bb7f9c && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v6.0/cudnn-8.0-linux-x64-v6.0.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-8.0-linux-x64-v6.0.tgz" | sha256sum -c - && \
    gunzip cudnn-8.0-linux-x64-v6.0.tgz && \
    tar --no-same-owner -xf cudnn-8.0-linux-x64-v6.0.tar -C /usr/local && \
    rm cudnn-8.0-linux-x64-v6.0.tar && \
    ldconfig
