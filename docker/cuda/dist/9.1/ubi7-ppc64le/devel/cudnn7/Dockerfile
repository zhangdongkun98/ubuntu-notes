ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.1-devel-ubi7
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.0.5
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=68834ffe96c91fa1b13517a4b5b0358f8433ed2d30f146b7bb41dd0ea50c55ce && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.0.5/cudnn-9.1-linux-ppc64le-v7.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-9.1-linux-ppc64le-v7.tgz" | sha256sum -c - && \
    gunzip cudnn-9.1-linux-ppc64le-v7.tgz && \
    tar --no-same-owner -xf cudnn-9.1-linux-ppc64le-v7.tar -C /usr/local && \
    rm cudnn-9.1-linux-ppc64le-v7.tar && \
    ldconfig
