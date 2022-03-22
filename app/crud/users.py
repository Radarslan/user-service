from typing import Any
from typing import Dict
from typing import Union

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.users import Users
from app.schemas.v1.user import UserCreate
from app.schemas.v1.user import UserQueryParams
from app.schemas.v1.user import UserUpdate


class CRUDUsers(CRUDBase[Users, UserCreate, UserQueryParams, UserUpdate]):
    def create(
        self, db: Session, *, obj_in: Union[UserCreate, Dict[str, Any]]
    ) -> Users:
        if isinstance(obj_in, dict):
            obj_in_data = obj_in
        else:
            obj_in_data = jsonable_encoder(obj_in)
        obj_in_data.pop("emails", None)
        obj_in_data.pop("phone_numbers", None)
        db_obj = self.model(**obj_in_data)

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


users_crud = CRUDUsers(Users)
