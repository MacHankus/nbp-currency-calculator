from abc import ABC
from decimal import Decimal

from modules.currency.core.entities.currency_to_calculate_entity import CurrencyToCalculateEntity


class ExchangePort(ABC):
    def get_exchange(self, currency_to_calculate: CurrencyToCalculateEntity) -> Decimal:
        pass