from typing import Annotated
from fastapi import APIRouter, Body
from pydantic import Field
from modules.currency.adapters.api.dto.incoming.calculate_currency_dto import (
    IncomingCalculateCurrencyDTO,
)


from modules.currency.adapters.api.dto.outcoming.calculated_value_dto import (
    CalculatedValueDTO,
)

router = APIRouter()


@router.post("/currency/calculate")
def calculate_currency(
    body: Annotated[IncomingCalculateCurrencyDTO, Body(...)]
) -> CalculatedValueDTO:
    return CalculatedValueDTO(value=1)
