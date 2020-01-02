FROM python:3.5.7-slim-stretch

MAINTAINER Fatih Baltacı "baltacifatih14@gmail.com"

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --user --upgrade setuptools wheel twine

WORKDIR /workspace
