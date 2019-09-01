FROM python:3.7-alpine3.8

RUN mkdir /app
WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


COPY . .

ENV PYTHONPATH=/app:/app/backend-exercise
