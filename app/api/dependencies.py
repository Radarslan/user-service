from typing import Generator

from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from app.db.session import get_engine
from app.db.session import get_session


def get_db() -> Generator:
    engine = get_engine()
    db: Session = None
    try:
        db = get_session(engine)
        yield db
    except OperationalError:
        db.rollback()
        # TODO: check if HTTP error should be raised
    finally:
        db.close()
