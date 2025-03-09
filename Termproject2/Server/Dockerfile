FROM python:3

RUN mkdir src
ADD server.py /src/

RUN apt-get update \
 && pip install pyzmq

WORKDIR /src/
EXPOSE 5557