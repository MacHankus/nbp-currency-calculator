FROM python:3.11-alpine

RUN apt-get install libpq-dev python3-dev

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./src src
COPY ./tests tests
COPY ./pyproject.toml pyproject.toml 
COPY ./poetry.lock poetry.lock

RUN poetry install --only-root

ENTRYPOINT poetry run pytest