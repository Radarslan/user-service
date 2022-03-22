from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.core.utils.get_entity import get_entity_instance
from app.crud.phone_numbers import phone_numbers_crud
from app.crud.users import users_crud
from app.schemas.v1.phone_number import PhoneNumber
from app.schemas.v1.phone_number import PhoneNumberCreate
from app.schemas.v1.phone_number import PhoneNumberUpdate

router = APIRouter()


@router.post(
    "/{user_id}/phone_numbers",
    response_model=PhoneNumber,
    status_code=201,
    tags=["phone_numbers"],
)
async def create_phone_number(
    *,
    user_id: int = Path(...),
    db: Session = Depends(get_db),
    obj_in: PhoneNumberCreate,
) -> Any:
    obj_in.user_id = user_id
    return phone_numbers_crud.create(db=db, obj_in=obj_in)


@router.get(
    "/{user_id}/phone_numbers",
    response_model=List[PhoneNumber],
    tags=["phone_numbers"],
)
async def read_phone_numbers(
    *, user_id: int = Path(...), db: Session = Depends(get_db)
) -> Any:
    user = get_entity_instance(db, users_crud, user_id)
    return user.phone_numbers


@router.get(
    "/{user_id}/phone_numbers/{id}",
    response_model=PhoneNumber,
    tags=["phone_number"],
)
async def read_phone_number(
    *,
    user_id: int = Path(...),
    id: int = Path(...),
    db: Session = Depends(get_db),
) -> Any:
    mail = get_entity_instance(db, phone_numbers_crud, id)
    if mail.user_id != user_id:
        raise HTTPException(
            422,
            detail=f"phone number {mail.id} does not belong to user {user_id}",
        )
    return mail


@router.put(
    "/{user_id}/phone_numbers/{id}",
    response_model=PhoneNumber,
    tags=["phone_number"],
)
async def update_phone_number(
    *,
    user_id: int = Path(...),
    id: int = Path(...),
    db: Session = Depends(get_db),
    obj_in: PhoneNumberUpdate,
) -> Any:
    mail = get_entity_instance(db, phone_numbers_crud, id)
    if mail.user_id != user_id:
        raise HTTPException(
            422,
            detail=f"phone number {mail.id} does not belong to user {user_id}",
        )
    db_obj = get_entity_instance(db, phone_numbers_crud, id)
    return phone_numbers_crud.update(db, db_obj=db_obj, obj_in=obj_in)
