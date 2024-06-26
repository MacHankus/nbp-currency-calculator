FROM python:3.11.6-slim

RUN apt-get update 
RUN apt-get install libpq-dev -y python3-dev
RUN apt-get install build-essential -y
RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml pyproject.toml 
COPY ./poetry.lock poetry.lock
RUN poetry config virtualenvs.create false && poetry install --only main

COPY ./src src

COPY ./alembic alembic
COPY ./alembic.ini alembic.ini


CMD export PYTHONPATH="src" && poetry run alembic upgrade head && poetry run python src/main.py