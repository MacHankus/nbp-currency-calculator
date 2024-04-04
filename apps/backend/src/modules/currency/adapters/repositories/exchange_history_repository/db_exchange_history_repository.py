from typing import List
from dependency_injector.wiring import Provide
from dependency_injector.wiring import inject
from sqlalchemy.orm import Session

from db.exchange_history.models.exchange_history import ExchangeHistory
from modules.currency.core.entities.exchange_history_entity import ExchangeHistoryEntity
from modules.currency.core.entities.new_request_entity import NewRequestEntity
from modules.currency.core.ports.exchange_history_repository_port import (
    ExchangeHistoryRepositoryPort,
)
from sqlalchemy import select


class DBExchangeHistoryRepository(ExchangeHistoryRepositoryPort):
    @inject
    def __init__(self, db_session: Session = Provide["exchange_history_session"]):
        self.db_session = db_session

    def add(self, request_data: NewRequestEntity) -> None:
        new_request_history_row = ExchangeHistory(
            currency_from=request_data.currency_from,
            currency_to=request_data.currency_to,
            request_date=request_data.request_date,
            is_error=request_data.is_error,
            amount=request_data.amount,
            result=request_data.result,
        )

        with self.db_session:
            self.db_session.add(new_request_history_row)
            self.db_session.commit()

        return None

    def get(self) -> List[ExchangeHistoryEntity]:
        with self.db_session:
            history = self.db_session.query(ExchangeHistory).all()

            return [
                ExchangeHistoryEntity(
                    id=x.id,
                    currency_from=x.currency_from,
                    currency_to=x.currency_to,
                    request_date=x.request_date,
                    amount=x.amount,
                    is_error=x.is_error,
                    result=x.result,
                )
                for x in history
            ]
