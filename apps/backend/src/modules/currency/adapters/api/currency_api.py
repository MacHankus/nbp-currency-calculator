from typing import Annotated

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends

from modules.currency.adapters.api.dto.incoming.calculate_currency_dto import IncomingCalculateCurrencyDTO
from modules.currency.adapters.api.dto.outcoming.calculated_value_dto import CalculatedValueDTO
from modules.currency.core.ports.requests_history_repository_port import RequestsHistoryRepositoryPort

router = APIRouter()

@inject
@router.post("/currency/calculate")
async def calculate_currency(
    body: Annotated[IncomingCalculateCurrencyDTO, Body(...)],
    repository: RequestsHistoryRepositoryPort = Depends(Provide["requests_history_repository"])
) -> CalculatedValueDTO:
    return CalculatedValueDTO(value=1)
