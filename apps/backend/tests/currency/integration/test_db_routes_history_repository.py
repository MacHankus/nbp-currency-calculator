from datetime import datetime

import pytest
from dependency_injector.containers import DeclarativeContainer
from sqlalchemy.ext.asyncio import AsyncSession

from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.random import get_random_decimal


@pytest.mark.asyncio
def test_should_add_row_to_request_history_table(
    container: DeclarativeContainer, requests_history_session: AsyncSession
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
