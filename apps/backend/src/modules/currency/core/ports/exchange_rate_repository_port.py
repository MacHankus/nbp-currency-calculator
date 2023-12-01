from abc import ABC, abstractmethod
from decimal import Decimal

from modules.currency.core.enums.currency_enum import CurrencyEnum


class ExchangeRateRepositoryPort(ABC):
    @abstractmethod
    async def get_exchange_rate(self, currency: CurrencyEnum) -> Decimal:
        pass