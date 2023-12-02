from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel

from modules.currency.core.enums.currency_enum import CurrencyEnum


class NewRequestEntity(BaseModel):
    currency_from: CurrencyEnum
    currency_to: CurrencyEnum
    request_date: datetime
    exchange_rate: Decimal
    is_error: bool
