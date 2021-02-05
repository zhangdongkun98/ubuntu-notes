ARG IMAGE_NAME
FROM ${IMAGE_NAME}:9.2-base-ubi8
LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

RUN yum install -y \
        cuda-libraries-$CUDA_PKG_VERSION \
cuda-nvtx-$CUDA_PKG_VERSION \
&& \
    rm -rf /var/cache/yum/*