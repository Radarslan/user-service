from typing import Any
from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CreateSchemaType
from app.crud.base import CRUDBase
from app.crud.emails import emails_crud
from app.crud.phone_numbers import phone_numbers_crud
from app.crud.users import users_crud
from app.models.users import Users
from app.schemas.v1.user import UserCreate
from app.schemas.v1.user import UserUpdate


def bl_create_user(db: Session, obj_in: UserCreate) -> Any:
    user = users_crud.create(db, obj_in=obj_in)
    user.emails = create_user_related_entities(
        db, user.id, emails_crud, obj_in.emails
    )
    user.phone_numbers = create_user_related_entities(
        db, user.id, phone_numbers_crud, obj_in.phone_numbers
    )
    return user


def create_user_related_entities(
    db: Session,
    user_id: int,
    entity_crud: CRUDBase,
    entities: List[CreateSchemaType],
) -> Any:
    created_entities = []
    for entity in entities:
        entity.user_id = user_id
        created_entities.append(entity_crud.create(db, obj_in=entity))
    return created_entities


def bl_delete_user(db: Session, db_obj: Users) -> Any:
    update_user = UserUpdate(is_active=False)
    return users_crud.update(db, db_obj=db_obj, obj_in=update_user)
