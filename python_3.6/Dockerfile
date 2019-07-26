FROM python:3.6

MAINTAINER Fatih Baltacı "baltacifatih14@gmail.com"

RUN apt-get update && apt-get install -y wget vim unzip zip curl

RUN pip install urwid==2.0.1 opencv-contrib-python==4.1.0.25

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace
