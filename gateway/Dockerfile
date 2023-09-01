# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

WORKDIR /servicegateway

RUN pip3 install flask
RUN pip install requests
RUN pip install flask_jwt_extended
RUN pip install requests
#ImportError: cannot import name 'encode' from 'jwt' (/usr/local/lib/python3.8/site-packages/jwt/__init__.py)

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]