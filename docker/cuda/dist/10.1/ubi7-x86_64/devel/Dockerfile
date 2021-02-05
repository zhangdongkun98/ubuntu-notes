ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-runtime-ubi7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

# setopt flag prevents yum from auto upgrading. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN yum install --setopt=obsoletes=0 -y \
    make \
    cuda-nvml-dev-$CUDA_PKG_VERSION \
    cuda-command-line-tools-$CUDA_PKG_VERSION \
    libcublas-devel-10.2.1.243-1 \
    cuda-cudart-dev-$CUDA_PKG_VERSION \
    cuda-libraries-dev-$CUDA_PKG_VERSION \
    cuda-minimal-build-$CUDA_PKG_VERSION \
    cuda-nvprof-$CUDA_PKG_VERSION \
    cuda-npp-dev-$CUDA_PKG_VERSION \
    && yum clean all \
    && rm -rf /var/cache/yum/*

RUN yum install -y xz && NCCL_DOWNLOAD_SUM=a58afe6d6467ead76a34867249942bca8b5b892f563611fb330ed0e5935e8878 && \
    curl -fsSL https://developer.download.nvidia.com/compute/redist/nccl/v2.8/nccl_2.8.3-1+cuda10.1_x86_64.txz -O && \
    echo "$NCCL_DOWNLOAD_SUM  nccl_2.8.3-1+cuda10.1_x86_64.txz" | sha256sum -c - && \
    unxz nccl_2.8.3-1+cuda10.1_x86_64.txz && \
    tar --no-same-owner --keep-old-files -xvf  nccl_2.8.3-1+cuda10.1_x86_64.tar -C /usr/local/cuda/include/ --strip-components=2 --wildcards '*/include/*' && \
    tar --no-same-owner --keep-old-files -xvf  nccl_2.8.3-1+cuda10.1_x86_64.tar -C /usr/local/cuda/lib64/ --strip-components=2 --wildcards '*/lib/libnccl.so' && \
    rm -f nccl_2.8.3-1+cuda10.1_x86_64.tar && \
    ldconfig

ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs