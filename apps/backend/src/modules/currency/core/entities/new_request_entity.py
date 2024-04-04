from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from modules.currency.core.enums.currency_enum import CurrencyEnum


class NewRequestEntity(BaseModel):
    currency_from: CurrencyEnum
    currency_to: CurrencyEnum
    request_date: datetime
    amount: float
    is_error: bool
    result: float
