import pytest
from sqlalchemy.orm import Session

from container import Container
from db.requests_history_db.connection import get_session


@pytest.fixture(scope='session')
def container():
    container = Container()
    yield container

@pytest.fixture
async def requests_history_session() -> Session:
    with get_session() as session:
        yield session