

import httpx
from loguru import logger
from pydantic import ValidationError

from modules.currency.adapters.repositories.exchange_rate_repository.dto.incoming_exchange_rate_dto import \
    IncomingExchangeRateDTO
from modules.currency.core.enums.currency_enum import CurrencyEnum
from modules.currency.core.ports.exchange_rate_repository_port import ExchangeRateRepositoryPort
from shared.exceptions.server_failed_request_error import ServerFailedRequestError
from shared.exceptions.server_unavailable_error import ServerUnavailableError


class HTTPExchangeRateRepository(ExchangeRateRepositoryPort):
    API_BASE_PATH = "https://api.nbp.pl/api/exchangerates/rates/a/{currency}/"
    HEADERS= {
        "Accept": "application/json"
    }
    def get_exchange_rate(self, currency: CurrencyEnum) -> float:
        with httpx.Client(headers=self.HEADERS) as client:
            prepared_path = self.API_BASE_PATH.format(currency=currency.value)
            try:
                response = client.get(prepared_path)
                response.raise_for_status()
            except httpx.RequestError:
                logger.exception(f"Request failed for path [{prepared_path}]")
                raise ServerUnavailableError()
            except httpx.HTTPStatusError:
                logger.exception(f"Request under path [{prepared_path}] responded with status code [{response.status_code}]")
                raise ServerFailedRequestError()
            
            try:
                response_model = IncomingExchangeRateDTO.model_validate_json(response.read())
            except ValidationError:
                logger.exception(f"Request under path [{prepared_path}] responded with incorrect content.")
                raise ServerFailedRequestError("Response cannot be validated")

            return response_model.rates[0].mid