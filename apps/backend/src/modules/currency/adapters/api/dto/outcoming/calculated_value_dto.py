from decimal import Decimal

from pydantic import BaseModel


class CalculatedValueDTO(BaseModel):
    value: Decimal