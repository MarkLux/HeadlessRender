FROM ubuntu:16.04

MAINTAINER liuminghao

RUN apt-get update && apt-get -y install \
    git wget python2.7 \
    python-pip python-dev build-essential

RUN pip install --upgrade pip

RUN pip install selenium && pip install thrift

WORKDIR /opt

RUN wget https://download-ssl.firefox.com.cn/releases/firefox/58.0/en-US/Firefox-latest-x86_64.tar.bz2 && tar -jxvf Firefox-latest-x86_64.tar.bz2

RUN cd /opt/firefox && wget https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz && \
    tar -zxvf geckodriver-v0.19.1-linux64.tar.gz

ENV PYTHONPATH ../
ENV PATH /opt/firefox:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

WORKDIR /home

RUN git clone https://github.com/MarkLux/HeadlessRender.git

EXPOSE 8080

WORKDIR /home/HeadlessRender/service

CMD python server.py