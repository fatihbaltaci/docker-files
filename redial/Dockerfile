FROM python:3.8-alpine

RUN apk add --no-cache mc openssh

RUN pip install --upgrade pip
RUN pip --no-cache-dir install redial

ENTRYPOINT ["redial"]
