from abc import ABC
from abc import abstractmethod

from modules.currency.core.entities.new_request_entity import NewRequestEntity


class RequestsHistoryRepositoryPort(ABC):

    @abstractmethod
    def add(self, request_data: NewRequestEntity) -> None:
        pass