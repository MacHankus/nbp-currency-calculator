
from pydantic import Field

from modules.currency.core.enums.currency_enum import CurrencyEnum
from shared.models.camel_model import CamelModel


class IncomingCalculateCurrencyDTO(CamelModel):
    currency_from: CurrencyEnum = Field(..., description="Base currency you want to exchange." )
    currency_to: CurrencyEnum = Field(..., description="Target currency." )
    value: float = Field(..., description="Value of base currency." )