FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app

#FROM tiangolo/uvicorn-gunicorn:python3.8
#
#LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"
#
#COPY requirements.txt /tmp/requirements.txt
#RUN pip install --no-cache-dir -r /tmp/requirements.txt
#
#COPY ./app /app