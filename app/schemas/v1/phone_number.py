import re
from typing import Optional

from pydantic import BaseModel
from pydantic import validator

from app.core.settings import data_validation


class PhoneNumberBase(BaseModel):
    number: Optional[str]

    @validator("number")
    def phone_validation(cls, value):
        regex = r"^(\(?([\d \-\)\–\+\(]+\/?){6,}\)?([ .\-–\/]?)([\d]+))$"
        is_valid = re.search(regex, value)
        if (
            not value
            or not len(value) >= data_validation.phone_number_min_length
            or not len(value) <= data_validation.phone_number_max_length
            or not is_valid
        ):
            raise ValueError("Invalid Phone Number")
        return value

    class Config:
        schema_extra = {"example": {"number": "+4915179536772"}}


# Properties to receive via API on creation
class PhoneNumberCreate(PhoneNumberBase):
    number: str
    user_id: Optional[int]


# Properties to receive via API on update
class PhoneNumberUpdate(PhoneNumberBase):
    pass


class PhoneNumberInDBBase(PhoneNumberBase):
    id: int
    number: str
    user_id: int

    class Config:
        orm_mode = True


# Additional properties to return via API
class PhoneNumber(PhoneNumberInDBBase):
    pass
