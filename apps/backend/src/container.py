from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.containers import WiringConfiguration

from db.requests_history.connection import get_session
from modules.currency.adapters.repositories.exchange_rate_repository.http_exchange_rate_repository import \
    HTTPExchangeRateRepository
from modules.currency.adapters.repositories.requests_history_repository.db_requests_history_repository import \
    DBRequestsHistoryRepository
from modules.currency.core.services.exchange_service import ExchangeService


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            "modules.currency.adapters.repositories.requests_history_repository.db_requests_history_repository",
            "modules.currency.core.services.exchange_service",
            "modules.currency.adapters.api.currency_api",
        ]
    )
    requests_history_session = providers.Resource(get_session)

    requests_history_repository = providers.Factory(DBRequestsHistoryRepository)

    exchange_rate_repository = providers.Factory(HTTPExchangeRateRepository)

    exchange_service = providers.Factory(ExchangeService)