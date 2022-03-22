from sqlalchemy.orm import Session

from app.core.business_logic_layer.users import bl_create_user
from app.schemas.v1.user import UserCreate


def test_create_user(db: Session, user_dict: dict) -> None:
    user = UserCreate(**user_dict)
    got_user = bl_create_user(db=db, obj_in=user)
    assert user_dict.get("first_name", None) == got_user.first_name
    assert user_dict.get("last_name", None) == got_user.last_name
    assert user_dict.get("emails", None) == got_user.emails
    assert user_dict.get("phone_numbers", None) == got_user.phone_numbers
    assert user_dict.get("is_active", None) == got_user.is_active
