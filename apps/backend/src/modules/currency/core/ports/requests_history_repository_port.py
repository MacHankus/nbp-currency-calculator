from abc import ABC
from abc import abstractmethod
from typing import Any, Coroutine

from modules.currency.core.entities.new_request_entity import NewRequestEntity


class RequestsHistoryRepositoryPort(ABC):

    @abstractmethod
    async def add(self, request_data: NewRequestEntity) -> None:
        pass