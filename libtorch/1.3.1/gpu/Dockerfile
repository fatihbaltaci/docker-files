FROM ubuntu:18.04

LABEL maintainer="baltacifatih14@gmail.com"

RUN apt-get update && apt-get install -y wget vim unzip zip curl cmake

RUN cd /opt &&  \
    wget -O libtorch_1.3.1.zip https://download.pytorch.org/libtorch/cu101/libtorch-cxx11-abi-shared-with-deps-1.3.1.zip && \
    unzip libtorch_1.3.1.zip && \
    rm libtorch_1.3.1.zip

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /opt/libtorch
