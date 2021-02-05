ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.2-devel-ubi7
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV CUDNN_VERSION 7.6.5.33
LABEL com.nvidia.cudnn.version="${CUDNN_VERSION}"

RUN yum install -y \
    libcudnn7-devel-${CUDNN_VERSION}-1.cuda10.2 \
    && yum clean all \
    && rm -rf /var/cache/yum/*
