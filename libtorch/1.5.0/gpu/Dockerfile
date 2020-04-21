FROM nvidia/cuda:10.2-cudnn7-devel-ubuntu18.04

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget vim unzip zip curl cmake gdb gdbserver tzdata && rm -rf /var/lib/apt/lists/*

RUN cd /opt &&  \
    wget -q -O libtorch_1.5.0 https://download.pytorch.org/libtorch/cu102/libtorch-cxx11-abi-shared-with-deps-1.5.0.zip && \
    unzip -q libtorch_1.5.0 && \
    rm libtorch_1.5.0

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /opt/libtorch
