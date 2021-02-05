
ARG IMAGE_NAME
FROM ${IMAGE_NAME}:11.2.0-runtime-ubuntu18.04

LABEL maintainer "NVIDIA CORPORATION <cudatools@nvidia.com>"

RUN apt-get update && apt-get install -y --no-install-recommends \
    cuda-cudart-dev-11-2=11.2.72-1 \
    cuda-command-line-tools-11-2=11.2.0-1 \
    cuda-minimal-build-11-2=11.2.0-1 \
    cuda-libraries-dev-11-2=11.2.0-1 \
    cuda-nvml-dev-11-2=11.2.67-1 \
    libnpp-dev-11-2=11.2.1.68-1 \
    libcublas-dev-11-2=11.3.1.68-1 \
    libcusparse-11-2=11.3.1.68-1 \
    libcusparse-dev-11-2=11.3.1.68-1 \
    && rm -rf /var/lib/apt/lists/*

# apt from auto upgrading the cublas package. See https://gitlab.com/nvidia/container-images/cuda/-/issues/88
RUN apt-mark hold libcublas-dev-11-2
ENV LIBRARY_PATH /usr/local/cuda/lib64/stubs