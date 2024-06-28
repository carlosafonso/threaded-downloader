#FROM ubuntu:23.10
FROM python:3.12.4-bookworm

RUN apt-get -y update && \
    apt-get -y install curl

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ .
