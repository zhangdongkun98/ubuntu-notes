ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.0-base-ubi8
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

RUN yum install -y \
        cuda-libraries-$CUDA_PKG_VERSION \
cuda-cublas-9-0-9.0.176.4-1 \
    && \
    rm -rf /var/cache/yum/*