FROM python:3.7

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget vim unzip zip curl tzdata make && rm -rf /var/lib/apt/lists/*

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN cd /opt && wget -q http://download.redis.io/releases/redis-6.0.5.tar.gz && \
    tar xvzf redis-6.0.5.tar.gz && \
    cd redis-6.0.5 && \
    make && make test && \
    make install

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace
