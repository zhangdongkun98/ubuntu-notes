ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.0-runtime-ubi8

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.6

RUN yum install -y \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    cuda-cudart-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    libcublas-devel-10.1.0.105-1 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

RUN yum install -y xz && NCCL_DOWNLOAD_SUM=57ab59ea45afe76ba5de6ced5e73c3bef1d7afc089fe1ad75128fc9890116adb && \
    curl -fsSL https://developer.download.nvidia.com/compute/redist/nccl/v2.6/nccl_2.6.4-1+cuda10.0_x86_64.txz -O && \
    echo "$NCCL_DOWNLOAD_SUM  nccl_2.6.4-1+cuda10.0_x86_64.txz" | sha256sum -c - && \
    unxz nccl_2.6.4-1+cuda10.0_x86_64.txz && \
    tar --no-same-owner --keep-old-files -xvf  nccl_2.6.4-1+cuda10.0_x86_64.tar -C /usr/local/cuda/include/ --strip-components=2 --wildcards '*/include/*' && \
    tar --no-same-owner --keep-old-files -xvf  nccl_2.6.4-1+cuda10.0_x86_64.tar -C /usr/local/cuda/lib64/ --strip-components=2 --wildcards '*/lib/libnccl.so' && \
    rm -f nccl_2.6.4-1+cuda10.0_x86_64.tar && \
    ldconfig

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs