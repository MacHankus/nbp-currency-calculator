from pydantic import BaseModel, Field
from decimal import Decimal

from modules.currency.core.enums.currency_enum import CurrencyEnum

class IncomingCalculateCurrencyDTO(BaseModel):
    currency_from: CurrencyEnum 
    currency_to: CurrencyEnum
    value: Decimal