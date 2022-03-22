from app.crud.base import CRUDBase
from app.models.phone_numbers import PhoneNumbers
from app.schemas.v1.phone_number import PhoneNumberCreate
from app.schemas.v1.phone_number import PhoneNumberUpdate


class CRUDPhoneNumbers(
    CRUDBase[PhoneNumbers, PhoneNumberCreate, None, PhoneNumberUpdate]
):
    pass


phone_numbers_crud = CRUDPhoneNumbers(PhoneNumbers)
