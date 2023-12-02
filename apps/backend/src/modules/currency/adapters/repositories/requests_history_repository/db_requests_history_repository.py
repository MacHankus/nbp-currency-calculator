from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from sqlalchemy.ext.asyncio import AsyncSession
from db.requests_history_db.models.request_history import RequestHistory

from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.ports.requests_history_repository_port import (
    RequestsHistoryRepositoryPort,
)


class DBRequestsHistoryRepository(RequestsHistoryRepositoryPort):
    @inject
    def __init__(
        self, db_session: AsyncSession = Provide["requests_history_db_session"]
    ):
        self.db_session = db_session

    async def add(self, request_data: NewRequestEntity) -> None:
        new_request_history_row = RequestHistory(
            currency_from=request_data.currency_from,
            currency_to=request_data.currency_to,
            request_date=request_data.request_date,
            is_error=request_data.is_error,
            exchange_rate=request_data.exchange_rate,
        )

        async with self.db_session:
            self.db_session.add(new_request_history_row)
            await self.db_session.commit()
