FROM ubuntu:18.04

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget git vim unzip zip curl cmake tzdata && rm -rf /var/lib/apt/lists/*

RUN cd /opt &&  \
    wget -q -O libtorch_1.3.1.zip https://download.pytorch.org/libtorch/cpu/libtorch-cxx11-abi-shared-with-deps-1.3.1%2Bcpu.zip && \
    unzip -q libtorch_1.3.1.zip && \
    rm libtorch_1.3.1.zip

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /opt/libtorch
