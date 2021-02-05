ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.0-devel-centos8
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.6.5.32
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=600267f2caaed2fd58eb214ba669d8ea35f396a7d19b94822e6b36f9f7088c20 && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.6.5/cudnn-10.0-linux-x64-v7.6.5.32.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-10.0-linux-x64-v7.6.5.32.tgz" | sha256sum -c - && \
    tar --no-same-owner -xzf cudnn-10.0-linux-x64-v7.6.5.32.tgz -C /usr/local && \
    rm cudnn-10.0-linux-x64-v7.6.5.32.tgz && \
    ldconfig
