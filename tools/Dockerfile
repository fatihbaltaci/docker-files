FROM ubuntu:18.04

LABEL maintainer="baltacifatih14@gmail.com"

RUN apt-get update && \
    apt-get install -y wget \
                       vim \
                       unzip \
                       zip \
                       curl \
                       net-tools \
                       ffmpeg \
                       netcat \
                       telnet \
                       tzdata && \
    rm -rf /var/lib/apt/lists/*

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace
