ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.0-runtime-ubi8
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.6.2.24
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=787adab5287597bf9a6462be4bcd55904593690315a889884d8ccfa8aaa9e370 && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.6.2/cudnn-9.0-linux-x64-v7.6.2.24.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-9.0-linux-x64-v7.6.2.24.tgz" | sha256sum -c - && \
    tar --no-same-owner -xzf cudnn-9.0-linux-x64-v7.6.2.24.tgz -C /usr/local --wildcards 'cuda/lib64/libcudnn.so.*' && \
    rm cudnn-9.0-linux-x64-v7.6.2.24.tgz && \
    ldconfig
