from datetime import datetime
from typing import Callable

import pytest
from dependency_injector.containers import DeclarativeContainer
from sqlalchemy.orm import Session

from db.exchange_history.models.exchange_history import ExchangeHistory
from modules.currency.adapters.repositories.exchange_history_repository.db_exchange_history_repository import \
    DBExchangeHistoryRepository
from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.db_exchange_history import get_exchange_history
from tests.helpers.db_exchange_history import truncate_exchange_history
from tests.helpers.random import get_random_float


@pytest.fixture(autouse=True, scope="module")
def fixture_truncate_request_history_at_start(exchange_history_session: Session):
    truncate_exchange_history(session=exchange_history_session)


@pytest.fixture(autouse=True)
def fixture_truncate_request_history(exchange_history_session: Session):
    yield
    truncate_exchange_history(session=exchange_history_session)


@pytest.mark.asyncio
def test_should_add_row_to_exchange_history_table(
    container: DeclarativeContainer, exchange_history_session: Session
):
    # Arrange
    repository: DBExchangeHistoryRepository = container.exchange_history_repository()
    new_request_entity = NewRequestEntity(
        currency_from=CurrencyEnum.PLN,
        currency_to=CurrencyEnum.PLN,
        request_date=datetime.now(),
        amount=get_random_float(),
        is_error=False,
        result=get_random_float(),
    )
    # Act

    repository.add(new_request_entity)

    # Assert
    requests_history = get_exchange_history(session=exchange_history_session)

    assert len(requests_history) == 1
    request = requests_history[0]

    assert request.currency_from == new_request_entity.currency_from
    assert request.currency_to == new_request_entity.currency_to
    assert request.request_date == new_request_entity.request_date
    assert float(request.amount) == float(new_request_entity.amount)
    assert request.is_error == new_request_entity.is_error
    assert float(request.result) == float(new_request_entity.result)


@pytest.mark.asyncio
def test_should_get_rows_from_exchange_history_table(
    container: DeclarativeContainer, exchange_history_session: Session, create_exchange_history: Callable[..., ExchangeHistory]
):
    # Arrange
    repository: DBExchangeHistoryRepository = container.exchange_history_repository()
    exchange_history = create_exchange_history(
        session=exchange_history_session,
        currency_from=CurrencyEnum.PLN,
        currency_to=CurrencyEnum.PLN,
        request_date=datetime.now(),
    )

    # Act

    history = repository.get()

    # Assert

    assert len(history) == 1
    echange_history_db = history[0]

    assert echange_history_db.currency_from == exchange_history.currency_from
    assert echange_history_db.currency_to == exchange_history.currency_to
    assert echange_history_db.request_date == exchange_history.request_date
    assert float(echange_history_db.amount) == float(exchange_history.amount)
    assert echange_history_db.is_error == exchange_history.is_error
    assert float(echange_history_db.result) == float(exchange_history.result)
