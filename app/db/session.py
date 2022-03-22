from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.core.settings import settings


def get_engine() -> Engine:
    return create_engine(
        url=settings.SQLALCHEMY_DATABASE_URI,
        pool_pre_ping=True,
    )


def get_session(engine: Engine) -> Session:
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)()
