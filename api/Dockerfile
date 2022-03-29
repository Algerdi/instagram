FROM python:3.10.2-alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev postgresql-dev

WORKDIR /api

COPY . .

RUN python -m pip install --upgrade pip
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN pip install poetry
RUN poetry install
