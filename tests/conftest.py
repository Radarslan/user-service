from typing import Generator

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.db.session import get_engine
from app.db.session import get_session
from app.main import app
from app.models.emails import Emails
from app.models.phone_numbers import PhoneNumbers
from app.models.users import Users
from tests.utils.emails import create_random_email
from tests.utils.emails import create_random_email_dict
from tests.utils.phone_numbers import create_random_phone_number
from tests.utils.phone_numbers import create_random_phone_number_dict
from tests.utils.users import create_random_user
from tests.utils.users import create_random_user_dict


@pytest.fixture()
def db() -> Generator:
    yield get_session(get_engine())


@pytest.fixture()
def another_session_db() -> Generator:
    yield get_session(get_engine())


@pytest.fixture()
def test_user() -> Generator:
    with TestClient(app) as test_user:
        yield test_user


@pytest.fixture
def user_dict() -> dict:
    return create_random_user_dict()


@pytest.fixture
def user(db: Session, user_dict: dict) -> Users:
    return create_random_user(db, user_dict)


@pytest.fixture
def email_dict(user: Users) -> dict:
    return create_random_email_dict()


@pytest.fixture
def email(db: Session, email_dict: dict) -> Emails:
    return create_random_email(db, email_dict)


@pytest.fixture
def phone_number_dict(user: Users) -> dict:
    return create_random_phone_number_dict()


@pytest.fixture
def phone_number(db: Session, phone_number_dict: dict) -> PhoneNumbers:
    return create_random_phone_number(db, phone_number_dict)
