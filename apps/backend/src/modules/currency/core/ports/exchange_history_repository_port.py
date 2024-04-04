from abc import ABC
from abc import abstractmethod
from typing import List

from modules.currency.core.entities.exchange_history_entity import ExchangeHistoryEntity
from modules.currency.core.entities.new_request_entity import NewRequestEntity


class ExchangeHistoryRepositoryPort(ABC):

    @abstractmethod
    def add(self, request_data: NewRequestEntity) -> None:
        pass

    @abstractmethod
    def get(self) -> List[ExchangeHistoryEntity]:
        pass