from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

from modules.currency.core.entities.exchange_history_entity import ExchangeHistoryEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum


class ExchangeHistoryDTO(BaseModel):
    id: int
    currency_from: CurrencyEnum
    currency_to: CurrencyEnum
    request_date: datetime
    amount: Optional[float] = None
    is_error: bool = False
    result: Optional[float] = None

    @classmethod
    def from_entity(cls, entity: ExchangeHistoryEntity) -> "ExchangeHistoryDTO":
        return ExchangeHistoryDTO(
            id=entity.id,
            currency_from=entity.currency_from,
            currency_to=entity.currency_to,
            request_date=entity.request_date,
            amount=entity.amount,
            is_error=entity.is_error,
            result=entity.result,
        )


class ExchangeHistoryResponseDTO(BaseModel):
    exchange_history: List[ExchangeHistoryDTO]
