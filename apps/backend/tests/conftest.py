from typing import Generator

import pytest
from sqlalchemy.orm import Session

from container import Container
from db.requests_history.connection import get_session


@pytest.fixture(scope="session")
def container():
    container = Container()
    yield container


@pytest.fixture(scope="session")
def requests_history_session() -> Generator[Session, None, None]:
    yield from get_session()
