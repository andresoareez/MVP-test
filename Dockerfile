FROM python:3.6
MAINTAINER Paulo Soares
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY ua-2*ks81n!-1f58q7!zz6al(w-3f*b4r4ympaygc6dy81yxb-
WORKDIR /apiapp
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
libsqlite3-dev
RUN pip install -U pip setuptools
COPY ./requirements.txt /apiapp/requirements.txt
RUN pip install -r /apiapp/requirements.txt

ADD . /apiapp/
EXPOSE 8000