FROM python:3.7-alpine
MAINTAINER Wajeeh Ul Hassan

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
# we added the package manager which comes with alpine
# we doing these for postgres
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev
# thats all for postgre
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user