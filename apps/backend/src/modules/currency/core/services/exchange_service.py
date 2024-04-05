from datetime import datetime
from typing import List

from dependency_injector.wiring import Provide

from modules.currency.core.entities.currency_to_calculate_entity import CurrencyToCalculateEntity
from modules.currency.core.entities.exchange_history_entity import ExchangeHistoryEntity
from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.enums.currency_enum import CurrencyEnum
from modules.currency.core.ports.exchange_history_repository_port import ExchangeHistoryRepositoryPort
from modules.currency.core.ports.exchange_port import ExchangePort
from modules.currency.core.ports.exchange_rate_repository_port import ExchangeRateRepositoryPort
from shared.exceptions.server_failed_request_error import ServerFailedRequestError
from shared.exceptions.server_unavailable_error import ServerUnavailableError


class ExchangeService(ExchangePort):
    def __init__(
        self,
        exchange_history_repository: ExchangeHistoryRepositoryPort = Provide[
            "exchange_history_repository"
        ],
        exchange_rate_repository: ExchangeRateRepositoryPort = Provide[
            "exchange_rate_repository"
        ],
    ):
        self.exchange_history_repository = exchange_history_repository
        self.exchange_rate_repository = exchange_rate_repository

    def get_exchange(self, currency_to_calculate: CurrencyToCalculateEntity) -> float:
        request_data = dict(
            currency_from=currency_to_calculate.currency_from,
            currency_to=currency_to_calculate.currency_to,
            request_date=datetime.now(),
        )
        try:
            rate_from = (
                self.exchange_rate_repository.get_exchange_rate(
                    currency_to_calculate.currency_from
                )
                if currency_to_calculate.currency_from != CurrencyEnum.PLN
                else 1
            )
            rate_to = (
                self.exchange_rate_repository.get_exchange_rate(
                    currency_to_calculate.currency_to
                )
                if currency_to_calculate.currency_to != CurrencyEnum.PLN
                else 1
            )
            base_value = rate_from * currency_to_calculate.value
            final_value = base_value / rate_to

            new_request_entity = NewRequestEntity(
                **request_data, result=final_value, amount=currency_to_calculate.value, is_error=False
            )
            self.exchange_history_repository.add(new_request_entity)

            return final_value

        except (ServerUnavailableError, ServerFailedRequestError):
            new_request_entity = NewRequestEntity(**request_data, is_error=True)
            self.exchange_history_repository.add(new_request_entity)

            raise

    def get_history(self) -> List[ExchangeHistoryEntity]:
        return self.exchange_history_repository.get()