# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /serviceauth

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD [ "python3", "authentication.py"]