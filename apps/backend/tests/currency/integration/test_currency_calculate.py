import itertools
from decimal import Decimal

import pytest

from modules.currency.adapters.api.dto.incoming.calculate_currency_dto import IncomingCalculateCurrencyDTO
from modules.currency.adapters.api.dto.outcoming.calculated_value_dto import CalculatedValueDTO
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.testclient import client

PATH = "/currency/calculate"


def test_response_should_return_200_when_provided_all_good_params():
    # Arrange
    payload = IncomingCalculateCurrencyDTO(
        currency_from="PLN", currency_to="USD", value=Decimal("1.1")
    )

    # Act
    response = client.post(PATH, json=payload.model_dump_json())

    # Assert
    assert response.status_code == 200


@pytest.mark.parametrize(
    "currency_from, currency_to", itertools.combinations(list(CurrencyEnum), 2)
)
def test_response_should_return_value_when_provided_all_good_params(
    currency_from, currency_to
):
    # Arrange
    payload = IncomingCalculateCurrencyDTO(
        currency_from=currency_from,
        currency_to=currency_to,
        value=Decimal("1.1"),
    )
    # Act
    response = client.post(PATH, json=payload.model_dump_json())

    response_model = CalculatedValueDTO.model_validate_json(response.read())

    # Assert
    assert response_model.value > 0
