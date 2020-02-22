FROM ubuntu:18.04

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget vim unzip zip curl cmake tzdata && rm -rf /var/lib/apt/lists/*

RUN cd /opt &&  \
    wget -q -O libtorch_1.4.0.zip https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-1.4.0%2Bcpu.zip && \
    unzip -q libtorch_1.4.0.zip && \
    rm libtorch_1.4.0.zip

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /opt/libtorch
