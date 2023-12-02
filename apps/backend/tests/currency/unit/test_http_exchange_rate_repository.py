import re
from datetime import datetime
from typing import Any
from typing import Dict

import pytest
from pytest_httpx import HTTPXMock

from modules.currency.adapters.repositories.exchange_rate_repository.dto.incoming_exchange_rate_dto import \
    IncomingExchangeRateDTO
from modules.currency.adapters.repositories.exchange_rate_repository.dto.incoming_exchange_rate_dto import RatesDTO
from modules.currency.adapters.repositories.exchange_rate_repository.http_exchange_rate_repository import \
    HTTPExchangeRateRepository
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.random import get_random_decimal
from tests.helpers.random import get_random_string

EXCHANGE_RATE_PATH_REGEXP = "https://api.nbp.pl/api/exchangerates/rates/a/.*"


def mock_exchange_rate_http_request(
    httpx_mock: HTTPXMock,
    json: Dict[Any, Any],
    status_code: int = None,
) -> None:
    url_pattern = re.compile(EXCHANGE_RATE_PATH_REGEXP)
    httpx_mock.add_response(url=url_pattern, status_code=status_code or 200, json=json)


@pytest.mark.parametrize("currency_enum", list(CurrencyEnum))
@pytest.mark.asyncio
async def test_should_get_exchange_rate_when_good_params_provided(
    httpx_mock: HTTPXMock, currency_enum: CurrencyEnum
):
    # Arrange
    repository = HTTPExchangeRateRepository()
    exchange_rate = get_random_decimal()
    payload = IncomingExchangeRateDTO(
        table=get_random_string(),
        currency=get_random_string(),
        code=get_random_string(),
        rates=RatesDTO(
            effective_date=datetime.now(),
            no=get_random_string(),
            mid=exchange_rate,
        ),
    )
    mock_exchange_rate_http_request(
        httpx_mock=httpx_mock, json=payload.model_dump_json()
    )

    # Act
    result = await repository.get_exchange_rate(currency_enum)

    # Assert

    assert result == exchange_rate
