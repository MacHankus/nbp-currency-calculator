from datetime import datetime

import pytest
from dependency_injector.containers import DeclarativeContainer
from sqlalchemy.orm import Session

from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.db_requests_history import get_requests_history, truncate_requests_history
from tests.helpers.random import get_random_decimal

@pytest.fixture(autouse=True)
def fixture_truncate_request_history(requests_history_session: Session):
    yield
    truncate_requests_history(session=requests_history_session)


@pytest.mark.asyncio
def test_should_add_row_to_request_history_table(
    container: DeclarativeContainer, requests_history_session: Session
):
    # Arrange
    repository = container.requests_history_repository()
    new_request_entity = NewRequestEntity(
        currency_from=CurrencyEnum.PLN,
        currency_to=CurrencyEnum.PLN,
        request_date=datetime.now(),
        exchange_rate=get_random_decimal(),
        is_error=False,
    )
    # Act

    repository.add(new_request_entity)

    # Assert
    requests_history = get_requests_history(session=requests_history_session)

    assert len(requests_history) == 1
    request = requests_history[0]

    assert request.currency_from == new_request_entity.currency_from
    assert request.currency_to== new_request_entity.currency_to
    assert request.request_date== new_request_entity.request_date
    assert request.exchange_rate== new_request_entity.exchange_rate
    assert request.is_error== new_request_entity.is_error
