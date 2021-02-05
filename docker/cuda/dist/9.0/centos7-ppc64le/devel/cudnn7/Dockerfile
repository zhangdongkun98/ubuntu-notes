ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.0-devel-centos7
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.2.1.38
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

# cuDNN license: https://developer.nvidia.com/cudnn/license_agreement
RUN CUDNN_DOWNLOAD_SUM=4c0937b5618cb0d1d7eed195b3a4ba6a49e061f9e734f5702b030c8522cdfc9c && \
    curl -fsSL http://developer.download.nvidia.com/compute/redist/cudnn/v7.2.1/cudnn-9.0-linux-ppc64le-v7.2.1.38.tgz -O && \
    echo "$CUDNN_DOWNLOAD_SUM  cudnn-9.0-linux-ppc64le-v7.2.1.38.tgz" | sha256sum -c - && \
    gunzip cudnn-9.0-linux-ppc64le-v7.2.1.38.tgz && \
    tar --no-same-owner -xf cudnn-9.0-linux-ppc64le-v7.2.1.38.tar -C /usr/local && \
    rm cudnn-9.0-linux-ppc64le-v7.2.1.38.tar && \
    ldconfig
