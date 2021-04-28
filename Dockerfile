FROM python:3.9-slim

RUN apt-get install build-dep -y python-psycopg2

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD . .

