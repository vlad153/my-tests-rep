# syntax=docker/dockerfile:1

FROM python:3.11-slim-buster

ARG POETRY_VERSION

WORKDIR /app

COPY . /app/.

RUN pip install "poetry==${POETRY_VERSION}"
RUN poetry config virtualenvs.create false
RUN poetry install --only main
