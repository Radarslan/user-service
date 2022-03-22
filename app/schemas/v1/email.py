from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr


class EmailBase(BaseModel):
    mail: Optional[EmailStr]

    class Config:
        schema_extra = {"example": {"mail": "user@example.com"}}


# Properties to receive via API on creation
class EmailCreate(EmailBase):
    mail: EmailStr
    user_id: Optional[int]


# Properties to receive via API on update
class EmailUpdate(EmailBase):
    pass


class EmailInDBBase(EmailBase):
    id: int
    mail: EmailStr
    user_id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class Email(EmailInDBBase):
    pass
