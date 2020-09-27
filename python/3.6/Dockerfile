FROM python:3.6

LABEL maintainer="baltacifatih14@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y wget vim unzip zip curl tzdata && rm -rf /var/lib/apt/lists/*

RUN pip install urwid==2.0.1 opencv-contrib-python==4.1.0.25

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace
