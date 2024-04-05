from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from modules.currency.core.enums.currency_enum import CurrencyEnum


class ExchangeHistoryEntity(BaseModel):
    id: int
    currency_from: CurrencyEnum
    currency_to: CurrencyEnum
    request_date: datetime
    amount: Optional[float] = None
    is_error: bool = False
    result: Optional[float] = None
