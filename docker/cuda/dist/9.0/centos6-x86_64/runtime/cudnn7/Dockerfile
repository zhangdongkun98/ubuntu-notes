ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.0-runtime-centos6
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.6.5.32
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=bd0a4c0090d5b02feec3f195738968690cc2470b9bc6026e6fe8ff245cd261c8 && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.6.5/cudnn-9.0-linux-x64-v7.6.5.32.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-9.0-linux-x64-v7.6.5.32.tgz" | sha256sum -c - && \
    tar --no-same-owner -xzf cudnn-9.0-linux-x64-v7.6.5.32.tgz -C /usr/local --wildcards 'cuda/lib64/libcudnn.so.*' && \
    rm cudnn-9.0-linux-x64-v7.6.5.32.tgz && \
    ldconfig
