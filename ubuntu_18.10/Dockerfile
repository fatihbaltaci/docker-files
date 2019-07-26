FROM ubuntu:18.10

MAINTAINER Fatih Baltacı "baltacifatih14@gmail.com"

RUN apt-get update && apt-get install -y wget vim unzip zip curl

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

WORKDIR /workspace
