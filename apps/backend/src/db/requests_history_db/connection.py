from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from settings import settings

CONNECTION_STRING = f"postgresql://{settings.DB_USERNAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

engine = create_engine(
    CONNECTION_STRING,
    echo=True,
    future=True,
)

session_factory = sessionmaker(engine)


def get_session() -> Generator[Session, None, None]:
    with session_factory() as session:
        yield session
