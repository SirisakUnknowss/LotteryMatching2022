# pull official base image
FROM python:3.9.18-bullseye

# Add build image as user
RUN groupadd docker
RUN useradd -M -u 501 -g docker unknowss
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# RUN python -m pip install pip
RUN python -m ensurepip --upgrade
RUN python -m pip install -U pip
RUN python -m pip install --upgrade setuptools
RUN apt update && apt-get upgrade -y
# Install Pillow dependencies
RUN apt install libxml2-dev libxslt-dev libffi-dev gcc curl
RUN apt install tk-dev tcl-dev
# install psycopg2 dependencies
RUN apt install gcc

WORKDIR /usr/src/app/
COPY ./docker/dev/requirements.txt ./docker/dev/requirements.txt

RUN pip install -r ./docker/dev/requirements.txt

USER unknowss

COPY . .