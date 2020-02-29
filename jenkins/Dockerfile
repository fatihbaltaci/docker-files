FROM jenkins/jenkins:lts

LABEL maintainer="baltacifatih14@gmail.com"

ARG DEBIAN_FRONTEND=noninteractive

USER root

RUN apt-get update && apt-get install -y wget vim unzip zip curl tzdata && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://get.docker.com/ | sh

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# change timezone
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime

RUN usermod -a -G docker jenkins
USER jenkins
