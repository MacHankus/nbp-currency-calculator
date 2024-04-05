from datetime import datetime

from sqlalchemy import DECIMAL
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class ExchangeHistory(Base):
    __tablename__ = "exchange_history"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    currency_from: Mapped[str] = mapped_column(String, nullable=False)
    currency_to: Mapped[str] = mapped_column(String, nullable=False)
    request_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    is_error: Mapped[bool] = mapped_column(Boolean, nullable=True)
    amount: Mapped[float] = mapped_column(DECIMAL, nullable=True)
    result: Mapped[float] = mapped_column(DECIMAL, nullable=True)
