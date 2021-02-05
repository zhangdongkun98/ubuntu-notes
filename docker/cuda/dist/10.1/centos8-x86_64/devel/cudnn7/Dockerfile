ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-devel-centos8
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.6.5.32
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=7eaec8039a2c30ab0bc758d303588767693def6bf49b22485a2c00bf2e136cb3 && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.6.5/cudnn-10.1-linux-x64-v7.6.5.32.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-10.1-linux-x64-v7.6.5.32.tgz" | sha256sum -c - && \
    gunzip cudnn-10.1-linux-x64-v7.6.5.32.tgz && \
    tar --no-same-owner -xf cudnn-10.1-linux-x64-v7.6.5.32.tar -C /usr/local && \
    rm cudnn-10.1-linux-x64-v7.6.5.32.tar && \
    ldconfig
