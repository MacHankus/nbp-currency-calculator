from typing import Annotated

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi.exceptions import HTTPException

from modules.currency.adapters.api.dto.incoming.calculate_currency_dto import IncomingCalculateCurrencyDTO
from modules.currency.adapters.api.dto.outcoming.calculated_value_dto import CalculatedValueDTO
from modules.currency.core.entities.currency_to_calculate_entity import CurrencyToCalculateEntity
from modules.currency.core.ports.exchange_port import ExchangePort
from shared.exceptions.server_failed_request_error import ServerFailedRequestError
from shared.exceptions.server_unavailable_error import ServerUnavailableError

router = APIRouter()


@router.post("/currency/calculate")
@inject
def calculate_currency(
    body: Annotated[IncomingCalculateCurrencyDTO, Body(...)],
    exchange_service: ExchangePort = Depends(Provide["exchange_service"]),
) -> CalculatedValueDTO:
    try:
        to_calculate = CurrencyToCalculateEntity(
            currency_from=body.currency_from,
            currency_to=body.currency_to,
            value=body.value,
        )
        calculated = exchange_service.get_exchange(to_calculate)

        return CalculatedValueDTO(value=calculated)
    except (ServerUnavailableError, ServerFailedRequestError):
        raise HTTPException(
            status_code=500, detail="Exchange server is unavailable. Try again later."
        )
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong")