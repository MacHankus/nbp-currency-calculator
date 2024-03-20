FROM python:3.11.6-slim

RUN apt-get install libpq-dev python3-dev

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./pyproject.toml pyproject.toml 
COPY ./poetry.lock poetry.lock
RUN poetry install --only-root

COPY alembic alembic
COPY alembic.ini alembic.ini
COPY ./src src
COPY ./tests tests


ENTRYPOINT poetry run pytest