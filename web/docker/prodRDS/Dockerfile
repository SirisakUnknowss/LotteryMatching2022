# pull official base image
FROM python:3.9.4-buster
# Add build image as user
RUN groupadd docker
RUN useradd -M -u 1000 -g docker ubuntu

# set work directory
WORKDIR /usr/src/app/

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN python -m pip install pip
RUN python -m pip install --upgrade pip setuptools
RUN apt update && apt-get upgrade -y
# Install Pillow dependencies
RUN apt-get install libxml2-dev libxslt-dev libffi-dev gcc curl
RUN apt-get install tk-dev tcl-dev
# install psycopg2 dependencies
RUN apt-get install gcc

COPY . .

RUN pip install -r ./docker/prodRDS/requirements.txt

USER ubuntu