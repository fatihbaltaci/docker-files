FROM nvidia/cuda:10.1-cudnn7-devel-ubuntu16.04

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget vim unzip zip curl cmake gdb gdbserver tzdata && rm -rf /var/lib/apt/lists/*

RUN cd /opt &&  \
    wget -q -O libtorch_1.4.0 https://download.pytorch.org/libtorch/cu101/libtorch-cxx11-abi-shared-with-deps-1.4.0.zip && \
    unzip -q libtorch_1.4.0 && \
    rm libtorch_1.4.0

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /opt/libtorch
