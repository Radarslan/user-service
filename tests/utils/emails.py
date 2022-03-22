from typing import Any
from typing import Dict

from sqlalchemy.orm import Session

from app.crud.emails import emails_crud
from app.models.emails import Emails
from app.models.users import Users


def create_random_email_dict(user: Users = None) -> Dict[str, Any]:
    return {"mail": user.emails[0], "user_id": user.id}


def create_random_email(db: Session, email_dict: dict) -> Emails:
    return emails_crud.create(db=db, obj_in=email_dict)
