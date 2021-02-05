ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-runtime-centos6
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 8.0.4.30
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=eb4b888e61715168f57a0a0a21c281ada6856b728e5112618ed15f8637487715 && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v8.0.4/cudnn-10.1-linux-x64-v8.0.4.30.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-10.1-linux-x64-v8.0.4.30.tgz" | sha256sum -c - && \
    tar --no-same-owner -xzf cudnn-10.1-linux-x64-v8.0.4.30.tgz -C /usr/local --wildcards 'cuda/lib64/libcudnn.so.*' && \
    rm cudnn-10.1-linux-x64-v8.0.4.30.tgz && \
    ldconfig
