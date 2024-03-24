from abc import ABC
from abc import abstractmethod

from modules.currency.core.entities.currency_to_calculate_entity import CurrencyToCalculateEntity


class ExchangePort(ABC):
    @abstractmethod
    def get_exchange(self, currency_to_calculate: CurrencyToCalculateEntity) -> float:
        pass