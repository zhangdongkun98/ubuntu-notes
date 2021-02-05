ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.2-devel-centos6
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 8.0.4.30
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=c12c69eb16698eacac40aa46b9ce399d4cd86efb6ff0c105142f8a28fcfb980e && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v8.0.4/cudnn-10.2-linux-x64-v8.0.4.30.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-10.2-linux-x64-v8.0.4.30.tgz" | sha256sum -c - && \
    tar --no-same-owner -xzf cudnn-10.2-linux-x64-v8.0.4.30.tgz -C /usr/local && \
    rm cudnn-10.2-linux-x64-v8.0.4.30.tgz && \
    ldconfig
