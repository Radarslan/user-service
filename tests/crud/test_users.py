from sqlalchemy.orm import Session

from app.crud.users import users_crud
from app.models.users import Users as UserModel
from app.schemas.v1.user import UserQueryParams


def test_create_users(db: Session, user_dict: dict) -> None:
    user = users_crud.create(db=db, obj_in=user_dict)
    assert user_dict.get("first_name", None) == user.first_name
    assert user_dict.get("last_name", None) == user.last_name
    assert user_dict.get("emails", None) == user.emails
    assert user_dict.get("phone_numbers", None) == user.phone_numbers
    assert user_dict.get("is_active", None) == user.is_active


def test_find_users(db: Session, user: UserModel) -> None:
    query = UserQueryParams(
        first_name=user.first_name[1:3],
        last_name=user.last_name[1:3],
        is_active=user.is_active,
    )
    users = users_crud.find_users(db=db, query=query)
    for got_user in users:
        assert (
            user.first_name[1:3] in got_user.first_name
            and user.last_name[1:3] in got_user.last_name
            and user.is_active == got_user.is_active
        )


def test_read_users(db: Session, user: UserModel) -> None:
    users = users_crud.read_many(db=db)
    for user in users:
        assert isinstance(user, UserModel)


def test_read_user(db: Session, user: UserModel) -> None:
    got_user = users_crud.read(db=db, entity_id=user.id)
    assert got_user is not None
    assert got_user.id == user.id
    assert got_user.first_name == user.first_name
    assert got_user.last_name == user.last_name
    assert got_user.emails == user.emails
    assert got_user.phone_numbers == user.phone_numbers
    assert got_user.is_active == user.is_active


def test_update_user(db: Session, user: UserModel, user_dict: dict) -> None:
    got_user = users_crud.update(db=db, db_obj=user, obj_in=user_dict)
    assert got_user.id == user.id
    assert user_dict.get("first_name", None) == user.first_name
    assert user_dict.get("last_name", None) == user.last_name
    assert user_dict.get("emails", None) == user.emails
    assert user_dict.get("phone_numbers", None) == user.phone_numbers
    assert user_dict.get("is_active", None) == user.is_active


def test_delete_user(db: Session, user: UserModel) -> None:
    got_user = users_crud.delete(db=db, entity_id=user.id)
    assert got_user is not None
    assert got_user.id == user.id
    assert got_user.first_name == user.first_name
    assert got_user.last_name == user.last_name
    assert got_user.emails == user.emails
    assert got_user.phone_numbers == user.phone_numbers
    assert got_user.is_active == user.is_active
