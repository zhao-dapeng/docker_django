FROM python:3.6

RUN mkdir /usr/src/app

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install cryptography

RUN pip install -r requirements.txt

EXPOSE 8080

