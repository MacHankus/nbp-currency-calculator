from decimal import Decimal
from unittest.mock import Mock

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from modules.currency.core.entities.currency_to_calculate_entity import CurrencyToCalculateEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from modules.currency.core.services.exchange_service import ExchangeService


def test_should_get_proper_rate(container: DeclarativeContainer):
    # Arrange
    mock_requests_history_repository = Mock()
    mock_exchange_rate_repository = Mock()
    mock_exchange_rate_repository__get_exchange_rate = Mock()
    usd_to_pln = Decimal("3.97")
    eur_to_pln = Decimal("5.05")
    final_eur = (2 * usd_to_pln) / eur_to_pln
    mock_exchange_rate_repository__get_exchange_rate.side_effect = [
        usd_to_pln,
        eur_to_pln,
    ]
    mock_exchange_rate_repository.get_exchange_rate = (
        mock_exchange_rate_repository__get_exchange_rate
    )

    to_calculate = CurrencyToCalculateEntity(
        currency_from=CurrencyEnum.USD, currency_to=CurrencyEnum.EUR, value=2
    )

    # Act
    with container.requests_history_repository.override(
        providers.Factory(lambda: mock_requests_history_repository)
    ), container.exchange_rate_repository.override(
        providers.Factory(lambda: mock_exchange_rate_repository)
    ):
        service: ExchangeService = container.exchange_service()
        returned_value = service.get_exchange(to_calculate)

    # Assert 

    assert returned_value == final_eur