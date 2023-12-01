from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

from shared.models.camel_model import CamelModel

# {"table":"A","currency":"frank szwajcarski","code":"CHF","rates":[{"no":"233/A/NBP/2023","effectiveDate":"2023-12-01","mid":4.5670}]}

class RatesDTO(CamelModel):
    no: str
    effective_date: datetime
    mid: Decimal


class IncomingExchangeRateDTO(BaseModel):
    table: str
    currency: str
    code: str
    rates: RatesDTO