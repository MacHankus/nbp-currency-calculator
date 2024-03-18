FROM python:3.11-slim

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./src src
COPY ./pyproject.toml pyproject.toml 
COPY ./poetry.lock poetry.lock

COPY ./alembic alembic
COPY ./alembic.ini alembic.ini

RUN poetry config virtualenvs.create false && poetry install --only main

CMD export PYTHONPATH="src" && poetry run alembic upgrade head && poetry run python src/main.py