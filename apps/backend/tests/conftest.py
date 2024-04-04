from typing import Generator

import pytest
from sqlalchemy.orm import Session

from container import Container
from db.exchange_history.connection import get_session
from helpers.db_exchange_history import create_exchange_history # noqa

@pytest.fixture(scope="session")
def container():
    container = Container()
    yield container


@pytest.fixture(scope="session")
def exchange_history_session() -> Generator[Session, None, None]:
    yield get_session()
