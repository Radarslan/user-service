from typing import Any
from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Path
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.core.utils.get_entity import get_entity_instance
from app.crud.emails import emails_crud
from app.crud.users import users_crud
from app.schemas.v1.email import Email
from app.schemas.v1.email import EmailCreate
from app.schemas.v1.email import EmailUpdate

router = APIRouter()


@router.post(
    "/{user_id}/emails", response_model=Email, status_code=201, tags=["emails"]
)
async def create_email(
    *,
    user_id: int = Path(...),
    db: Session = Depends(get_db),
    obj_in: EmailCreate,
) -> Any:
    obj_in.user_id = user_id
    return emails_crud.create(db=db, obj_in=obj_in)


@router.get("/{user_id}/emails", response_model=List[Email], tags=["emails"])
async def read_emails(
    *, user_id: int = Path(...), db: Session = Depends(get_db)
) -> Any:
    user = get_entity_instance(db, users_crud, user_id)
    return user.emails


@router.get("/{user_id}/emails/{id}", response_model=Email, tags=["email"])
async def read_email(
    *,
    user_id: int = Path(...),
    id: int = Path(...),
    db: Session = Depends(get_db),
) -> Any:
    mail = get_entity_instance(db, emails_crud, id)
    if mail.user_id != user_id:
        raise HTTPException(
            422, detail=f"email {mail.id} does not belong to user {user_id}"
        )
    return mail


@router.put("/{user_id}/emails/{id}", response_model=Email, tags=["email"])
async def update_email(
    *,
    user_id: int = Path(...),
    id: int = Path(...),
    db: Session = Depends(get_db),
    obj_in: EmailUpdate,
) -> Any:
    mail = get_entity_instance(db, emails_crud, id)
    if mail.user_id != user_id:
        raise HTTPException(
            422, detail=f"email {mail.id} does not belong to user {user_id}"
        )
    db_obj = get_entity_instance(db, emails_crud, id)
    return emails_crud.update(db, db_obj=db_obj, obj_in=obj_in)
