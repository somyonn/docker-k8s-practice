FROM python:3

RUN mkdir src
ADD client.py /src/

RUN apt-get update \
 && pip install pyzmq

WORKDIR /src/
EXPOSE 5557