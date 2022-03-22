from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Path
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.core.business_logic_layer.users import bl_create_user
from app.core.business_logic_layer.users import bl_delete_user
from app.core.settings import data_validation
from app.core.utils.get_entity import get_entity_instance
from app.crud.users import users_crud
from app.schemas.v1.user import User
from app.schemas.v1.user import UserCreate
from app.schemas.v1.user import UserQueryParams

router = APIRouter()


@router.post("/", response_model=User, status_code=201, tags=["users"])
async def create_user(
    *, db: Session = Depends(get_db), obj_in: UserCreate
) -> Any:
    return bl_create_user(db, obj_in=obj_in)


@router.get("/", response_model=List[User], tags=["users"])
async def find_users(
    *,
    db: Session = Depends(get_db),
    query: UserQueryParams = Depends(),
    skip: int = 0,
    limit: int = data_validation.page_size,
) -> Any:

    users = users_crud.find_many(db, query, skip, limit)
    return users


@router.get("/{id}", response_model=User, tags=["user"])
async def read_user(
    *, id: int = Path(...), db: Session = Depends(get_db)
) -> Any:
    return get_entity_instance(db, users_crud, id)


@router.delete("/{id}", response_model=User, tags=["user"])
async def delete_user(
    *, id: int = Path(...), db: Session = Depends(get_db)
) -> Any:
    db_obj = get_entity_instance(db, users_crud, id)
    return bl_delete_user(db=db, db_obj=db_obj)
