ARG IMAGE_NAME
FROM ${IMAGE_NAME}:8.0-devel-ubi7
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.0.2.38
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=7bc1452c9ac5ab4fda03e3226c83202c6c85431e2a3a51dce67ac0da6ffa45a8 && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.0.2/cudnn-8.0-linux-ppc64le-v7.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-8.0-linux-ppc64le-v7.tgz" | sha256sum -c - && \
    gunzip cudnn-8.0-linux-ppc64le-v7.tgz && \
    tar --no-same-owner -xf cudnn-8.0-linux-ppc64le-v7.tar -C /usr/local && \
    rm cudnn-8.0-linux-ppc64le-v7.tar && \
    ldconfig
