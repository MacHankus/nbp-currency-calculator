from decimal import Decimal
import re
from datetime import datetime
from typing import Any
from typing import Dict
from unittest.mock import AsyncMock, Mock

import pytest
from pytest_httpx import HTTPXMock

from modules.currency.adapters.repositories.exchange_rate_repository.dto.incoming_exchange_rate_dto import IncomingExchangeRateDTO
from modules.currency.adapters.repositories.exchange_rate_repository.dto.incoming_exchange_rate_dto import RatesDTO
from modules.currency.adapters.repositories.exchange_rate_repository.http_exchange_rate_repository import HTTPExchangeRateRepository
from modules.currency.adapters.repositories.requests_history_repository.db_requests_history_repository import DBRequestsHistoryRepository
from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.random import get_random_decimal
from tests.helpers.random import get_random_string

async def test_should_accept_argument():
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
    await repository.add(new_request)


async def test_should_call_session():
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
    await repository.add(new_request)

    # Assert
    assert mock_session_add.assert_called_once()
    assert mock_session_commit.assert_awaited_once()