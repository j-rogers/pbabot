# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /pbabot

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD [ "python3", "pbabot/main.py", "-g", "sprawlcustom" ]
