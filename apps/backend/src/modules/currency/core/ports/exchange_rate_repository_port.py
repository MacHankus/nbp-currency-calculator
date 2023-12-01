from abc import ABC, abstractmethod
from decimal import Decimal

from modules.currency.core.enums.currency_enum import CurrencyEnum


class ExchangeRateRepositoryPort(ABC):
    @abstractmethod
    def get_exchange_rate(currency: CurrencyEnum) -> Decimal:
        pass