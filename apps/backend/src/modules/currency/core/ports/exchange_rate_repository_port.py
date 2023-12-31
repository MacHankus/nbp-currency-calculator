from abc import ABC
from abc import abstractmethod
from decimal import Decimal

from modules.currency.core.enums.currency_enum import CurrencyEnum


class ExchangeRateRepositoryPort(ABC):
    @abstractmethod
    def get_exchange_rate(self, currency: CurrencyEnum) -> Decimal:
        pass