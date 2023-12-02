FROM python:3.11-slim

RUN pip install --upgrade pip
RUN pip install poetry

COPY ./src src
COPY ./pyproject.toml pyproject.toml 
COPY ./poetry.lock poetry.lock

RUN poetry config virtualenvs.create false && poetry install

RUN poetry run pip freeze

CMD poetry run python src/main.py