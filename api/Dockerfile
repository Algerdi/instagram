FROM python:3.10.2-alpine

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev postgresql-dev

WORKDIR /api

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry install
