from datetime import datetime
from unittest.mock import AsyncMock
from unittest.mock import Mock

from modules.currency.adapters.repositories.requests_history_repository.db_requests_history_repository import \
    DBRequestsHistoryRepository
from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.random import get_random_decimal


def test_should_accept_argument():
    # Arrange 
    mock_session = Mock()
    repository = DBRequestsHistoryRepository(db_session=mock_session)
    new_request = NewRequestEntity(
        currency_from=CurrencyEnum.PLN,
        currency_to=CurrencyEnum.PLN,
        request_date=datetime.now(),
        exchange_rate=get_random_decimal(),
        is_error=False

    )
    
    # Act
    repository.add(new_request)


def test_should_call_session():
    # Arrange 
    mock_session = AsyncMock()
    mock_session_add = AsyncMock()
    mock_session_commit = AsyncMock()
    mock_session.add = mock_session_add
    mock_session.commit = mock_session_commit
    repository = DBRequestsHistoryRepository(db_session=mock_session)
    new_request = NewRequestEntity(
        currency_from=CurrencyEnum.PLN,
        currency_to=CurrencyEnum.PLN,
        request_date=datetime.now(),
        exchange_rate=get_random_decimal(),
        is_error=False
    )
    
    # Act
    repository.add(new_request)

    # Assert
    assert mock_session_add.assert_called_once()
    assert mock_session_commit.assert_awaited_once()