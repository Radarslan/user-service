from typing import Any
from typing import Dict

from sqlalchemy.orm import Session

from app.crud.phone_numbers import phone_numbers_crud
from app.models.phone_numbers import PhoneNumbers
from app.models.users import Users


def create_random_phone_number_dict(user: Users = None) -> Dict[str, Any]:
    return {"number": user.phone_numbers[0], "user_id": user.id}


def create_random_phone_number(
    db: Session, phone_number_dict: dict
) -> PhoneNumbers:
    return phone_numbers_crud.create(db=db, obj_in=phone_number_dict)
