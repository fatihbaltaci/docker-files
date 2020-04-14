FROM python:3.5.7-slim-stretch

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y git tzdata vim && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --user --upgrade setuptools wheel twine

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace
