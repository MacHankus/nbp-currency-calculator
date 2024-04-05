from datetime import datetime
from typing import List
from typing import Optional

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

from db.exchange_history.models import ExchangeHistory
from modules.currency.core.enums.currency_enum import CurrencyEnum
from tests.helpers.random import get_random_float


def get_exchange_history(session: Session) -> List[ExchangeHistory]:
    return session.query(ExchangeHistory).all()


class Missing:
    pass


@pytest.fixture
def create_exchange_history(request: pytest.FixtureRequest) -> ExchangeHistory:
    def wrapped(
        session: Session,
        currency_from: Optional[CurrencyEnum],
        currency_to: Optional[CurrencyEnum],
        request_date: datetime,
        is_error: Optional[bool] = Missing,
        amount: Optional[float] = Missing,
        result: Optional[float] = Missing,
    ):
        new_exchange_history = ExchangeHistory(
            currency_from=currency_from,
            currency_to=currency_to,
            request_date=request_date,
            is_error=is_error if is_error is not Missing else False,
            amount=amount if amount is not Missing else get_random_float(),
            result=result if result is not Missing else get_random_float(),
        )
        session.add(new_exchange_history)
        session.commit()

        def finalizer():
            session.delete(new_exchange_history)
            session.commit()

        request.addfinalizer(finalizer)
        return new_exchange_history

    return wrapped


def truncate_exchange_history(session: Session) -> None:
    with session:
        session.execute(text(f"""TRUNCATE public.{ExchangeHistory.__tablename__}"""))
        session.commit()
