# syntax=docker/dockerfile:1
FROM python:3.10
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT bash -c ./docker-entrypoint.sh
