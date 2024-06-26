from typing import Annotated

from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi.exceptions import HTTPException
from loguru import logger

from modules.currency.adapters.api.dto.incoming.calculate_currency_dto import IncomingCalculateCurrencyDTO
from modules.currency.adapters.api.dto.outcoming.calculated_value_dto import CalculatedValueDTO
from modules.currency.adapters.api.dto.outcoming.exchange_history_response_dto import ExchangeHistoryDTO
from modules.currency.adapters.api.dto.outcoming.exchange_history_response_dto import ExchangeHistoryResponseDTO
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
        logger.exception("Server exception during currency calculate")
        raise HTTPException(
            status_code=500, detail="Exchange server is unavailable. Try again later."
        )
    except Exception:
        logger.exception("Unknown exception during currency calculate")
        raise HTTPException(status_code=500, detail="Something went wrong")


@router.get("/exchange/history")
@inject
def get_exchange_history(
    exchange_service: ExchangePort = Depends(Provide["exchange_service"]),
) -> ExchangeHistoryResponseDTO:
    try:
        exchange_history = exchange_service.get_history()
        return ExchangeHistoryResponseDTO(
            exchange_history=[
                ExchangeHistoryDTO.from_entity(x) for x in exchange_history
            ]
        )
    except Exception:
        logger.exception("Unknown exception during currency calculate")
        raise HTTPException(status_code=500, detail="Something went wrong")
