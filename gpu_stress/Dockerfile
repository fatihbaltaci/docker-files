FROM nvidia/cuda:11.0.3-cudnn8-devel-ubuntu18.04

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git wget vim unzip zip curl tzdata build-essential && rm -rf /var/lib/apt/lists/*

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /workspace

RUN git clone https://github.com/wilicc/gpu-burn.git

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

