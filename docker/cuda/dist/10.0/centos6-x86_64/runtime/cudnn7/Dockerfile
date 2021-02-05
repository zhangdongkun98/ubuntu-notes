ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.0-runtime-centos6
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.6.5.32
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=28355e395f0b2b93ac2c83b61360b35ba6cd0377e44e78be197b6b61b4b492ba && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.6.5/cudnn-10.0-linux-x64-v7.6.5.32.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-10.0-linux-x64-v7.6.5.32.tgz" | sha256sum -c - && \
    tar --no-same-owner -xzf cudnn-10.0-linux-x64-v7.6.5.32.tgz -C /usr/local --wildcards 'cuda/lib64/libcudnn.so.*' && \
    rm cudnn-10.0-linux-x64-v7.6.5.32.tgz && \
    ldconfig
