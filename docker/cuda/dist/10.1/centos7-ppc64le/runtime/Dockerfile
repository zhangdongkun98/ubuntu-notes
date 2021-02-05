ARG IMAGE_NAME
FROM ${IMAGE_NAME}:10.1-base-centos7

LABEL maintainer "NVIDIA CORPORATION <sw-cuda-installer@nvidia.com>"

ENV NCCL_VERSION 2.8.3

# setopt flag prevents yum from auto upgrading. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN yum install --setopt=obsoletes=0 -y \
    cuda-libraries-$CUDA_PKG_VERSION \
    cuda-nvtx-$CUDA_PKG_VERSION \
    cuda-npp-$CUDA_PKG_VERSION \
    libcublas10-10.2.1.243-1 \
    && yum clean all \
    && rm -rf /var/cache/yum/*

RUN yum install -y yum-plugin-versionlock && yum versionlock libcublas10

RUN yum install -y xz && NCCL_DOWNLOAD_SUM=ab31ca3def0c9108dd5934ca7562831a924cd7941762592963b7e4447c3d17da \
    && curl -fsSL https://developer.download.nvidia.com/compute/redist/nccl/v2.8/nccl_2.8.3-1+cuda10.1_ppc64le.txz -O \
    && echo "$NCCL_DOWNLOAD_SUM  nccl_2.8.3-1+cuda10.1_ppc64le.txz" | sha256sum -c - \
    && unxz nccl_2.8.3-1+cuda10.1_ppc64le.txz \
    && tar --no-same-owner --keep-old-files -xvf nccl_2.8.3-1+cuda10.1_ppc64le.tar -C /usr/local/cuda/lib64/ --strip-components=2 --wildcards '*/lib/libnccl.so.*' \
    && tar --no-same-owner --keep-old-files -xvf  nccl_2.8.3-1+cuda10.1_ppc64le.tar -C /usr/lib64/pkgconfig/ --strip-components=3 --wildcards '*/lib/pkgconfig/*' \
    && rm -f nccl_2.8.3-1+cuda10.1_ppc64le.tar \
    && ldconfig \
    && yum clean all \
    && rm -rf /var/cache/yum/*
