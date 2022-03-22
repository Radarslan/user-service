from typing import List
from typing import Optional

from fastapi import Query
from pydantic import BaseModel
from pydantic import constr

from app.core.settings import data_validation
from app.schemas.v1.email import Email
from app.schemas.v1.email import EmailCreate
from app.schemas.v1.phone_number import PhoneNumber
from app.schemas.v1.phone_number import PhoneNumberCreate


class UserQueryParams:
    __slots__ = ["first_name", "last_name", "is_active"]

    def __init__(
        self,
        first_name: Optional[str] = Query(
            None,
            min_length=data_validation.names_min_length,
            max_length=data_validation.first_name_max_length,
        ),
        last_name: Optional[str] = Query(
            None,
            min_length=data_validation.names_min_length,
            max_length=data_validation.last_name_max_length,
        ),
        is_active: Optional[bool] = Query(True),
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = is_active


class UserBase(BaseModel):
    first_name: Optional[
        constr(
            max_length=data_validation.last_name_max_length,
            min_length=data_validation.names_min_length,
        )
    ]
    last_name: Optional[
        constr(
            max_length=data_validation.first_name_max_length,
            min_length=data_validation.names_min_length,
        )
    ]
    is_active: Optional[bool] = True


# Properties to receive via API on creation
class UserCreate(UserBase):
    first_name: constr(
        max_length=data_validation.last_name_max_length,
        min_length=data_validation.names_min_length,
    )
    last_name: constr(
        max_length=data_validation.first_name_max_length,
        min_length=data_validation.names_min_length,
    )
    emails: List[EmailCreate]
    phone_numbers: List[PhoneNumberCreate]


# Properties to receive via API on update
class UserUpdate(UserBase):
    pass


class UserInDBBase(UserBase):
    id: int
    first_name: constr(max_length=data_validation.last_name_max_length)
    last_name: constr(max_length=data_validation.first_name_max_length)
    emails: List[Email]
    phone_numbers: List[PhoneNumber]
    is_active: bool = True

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass
