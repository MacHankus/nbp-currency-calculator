from abc import ABC
from abc import abstractmethod
from typing import List

from modules.currency.core.entities.currency_to_calculate_entity import CurrencyToCalculateEntity
from modules.currency.core.entities.exchange_history_entity import ExchangeHistoryEntity


class ExchangePort(ABC):
    @abstractmethod
    def get_exchange(self, currency_to_calculate: CurrencyToCalculateEntity) -> float:
        pass

    @abstractmethod
    def get_history(self) -> List[ExchangeHistoryEntity]:
        pass