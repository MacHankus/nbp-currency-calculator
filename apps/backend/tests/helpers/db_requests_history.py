from typing import List

from sqlalchemy import text
from sqlalchemy.orm import Session

from db.requests_history_db.models import RequestHistory


def get_requests_history(session: Session) -> List[RequestHistory]:
    return session.query(RequestHistory).all()

def truncate_requests_history(session: Session) -> None:
    with session:
        session.execute(text("""TRUNCATE public.request_history"""))
        session.commit()