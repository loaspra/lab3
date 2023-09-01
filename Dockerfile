# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /serviceconsumer

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5002

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]