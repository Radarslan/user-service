from app.crud.base import CRUDBase
from app.models.emails import Emails
from app.schemas.v1.email import EmailCreate
from app.schemas.v1.email import EmailUpdate


class CRUDEmails(CRUDBase[Emails, EmailCreate, None, EmailUpdate]):
    pass


emails_crud = CRUDEmails(Emails)
