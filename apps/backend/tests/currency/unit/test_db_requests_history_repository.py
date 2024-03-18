from datetime import datetime
from unittest.mock import MagicMock

from modules.currency.adapters.repositories.requests_history_repository.db_requests_history_repository import \
    DBRequestsHistoryRepository
from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.random import get_random_decimal


def test_should_accept_argument():
    # Arrange 
    mock_session = MagicMock()
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
    mock_session = MagicMock()
    mock_session_add = MagicMock()
    mock_session_commit = MagicMock()
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
    mock_session_add.assert_called_once()