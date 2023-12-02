from decimal import Decimal

from modules.currency.core.enums.currency_enum import CurrencyEnum
from shared.models.camel_model import CamelModel


class IncomingCalculateCurrencyDTO(CamelModel):
    currency_from: CurrencyEnum 
    currency_to: CurrencyEnum
    value: Decimal