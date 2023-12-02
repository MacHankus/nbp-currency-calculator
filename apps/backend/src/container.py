from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.containers import WiringConfiguration

from db.requests_history_db.connection import get_session
from modules.currency.adapters.repositories.requests_history_repository.db_requests_history_repository import \
    DBRequestsHistoryRepository


class Container(DeclarativeContainer):
    wiring_config = WiringConfiguration(
        modules=[
            "modules.currency.adapters.repositories.requests_history_repository.db_requests_history_repository"
        ]
    )
    requests_history_session = providers.Factory(get_session)

    requests_history_repository = providers.Factory(DBRequestsHistoryRepository)
