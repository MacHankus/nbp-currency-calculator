from decimal import Decimal

from pydantic import BaseModel

from modules.currency.core.enums.currency_enum import CurrencyEnum


class IncomingCalculateCurrencyDTO(BaseModel):
    currency_from: CurrencyEnum 
    currency_to: CurrencyEnum
    value: Decimal