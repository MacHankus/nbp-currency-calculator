from datetime import datetime
import itertools
from decimal import Decimal
from typing import Callable

import pytest

from modules.currency.adapters.api.dto.incoming.calculate_currency_dto import (
    IncomingCalculateCurrencyDTO,
)
from modules.currency.adapters.api.dto.outcoming.calculated_value_dto import (
    CalculatedValueDTO,
)
from modules.currency.adapters.api.dto.outcoming.exchange_history_response_dto import ExchangeHistoryResponseDTO
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.testclient import client

PATH = "/exchange/history"


def test_response_should_return_200_when_provided_all_good_params():
    # Act
    response = client.get(PATH)

    # Assert
    assert response.status_code == 200, response.text


def test_response_should_return_value_when_provided_all_good_params(
    exchange_history_session, create_exchange_history: Callable
):
    # Arrange
    exchange_history = create_exchange_history(
        session=exchange_history_session,
        currency_from=CurrencyEnum.PLN,
        currency_to=CurrencyEnum.PLN,
        request_date=datetime.now(),
    )

    # Act
    response = client.get(PATH)

    response_model = ExchangeHistoryResponseDTO.model_validate(response.json())

    # Assert
    assert len(response_model.exchange_history) == 1
