ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.2-runtime-centos6
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.6.5.32
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=a2a2c7a8ba7b16d323b651766ee37dcfdbc2b50d920f73f8fde85005424960e4 && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.6.5/cudnn-9.2-linux-x64-v7.6.5.32.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-9.2-linux-x64-v7.6.5.32.tgz" | sha256sum -c - && \
    tar --no-same-owner -xzf cudnn-9.2-linux-x64-v7.6.5.32.tgz -C /usr/local --wildcards 'cuda/lib64/libcudnn.so.*' && \
    rm cudnn-9.2-linux-x64-v7.6.5.32.tgz && \
    ldconfig
