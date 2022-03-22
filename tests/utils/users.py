from random import randint
from typing import Any
from typing import Dict

from sqlalchemy.orm import Session

from app.core.business_logic_layer.users import bl_create_user
from app.core.settings import data_validation
from app.models.users import Users
from app.schemas.v1.user import UserCreate
from tests.utils.common import get_random_boolean
from tests.utils.common import get_random_email_address
from tests.utils.common import get_random_lower_string
from tests.utils.common import get_random_phone_number


def create_random_user_dict() -> Dict[str, Any]:
    return {
        "first_name": get_random_lower_string(
            randint(
                data_validation.names_min_length + 2,
                data_validation.first_name_max_length,
            )
        ),
        "last_name": get_random_lower_string(
            randint(
                data_validation.names_min_length + 2,
                data_validation.last_name_max_length,
            )
        ),
        "is_active": get_random_boolean(),
        "emails": [get_random_email_address()],
        "phone_numbers": [get_random_phone_number()],
    }


def create_random_user(db: Session, user_dict: dict) -> Users:
    user = UserCreate(**user_dict)
    return bl_create_user(db=db, obj_in=user)
