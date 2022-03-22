from sqlalchemy.orm import Session

from app.crud.emails import emails_crud
from app.models.emails import Emails as EmailModel


def test_create_emails(db: Session, email_dict: dict) -> None:
    email = emails_crud.create(db=db, obj_in=email_dict)
    assert email_dict.get("mail", None) == email.mail
    assert email_dict.get("user_id", None) == email.user_id


def test_read_emails(db: Session, email: EmailModel) -> None:
    emails = emails_crud.read_many(db=db)
    for email in emails:
        assert isinstance(email, EmailModel)


def test_read_email(db: Session, email: EmailModel) -> None:
    got_email = emails_crud.read(db=db, entity_id=email.id)
    assert got_email is not None
    assert email.id == got_email.id
    assert email.mail == got_email.mail
    assert email.user_id == got_email.user_id


def test_update_email(
    db: Session, email: EmailModel, email_dict: dict
) -> None:
    got_email = emails_crud.update(db=db, db_obj=email, obj_in=email_dict)
    assert email.id == got_email.id
    assert email.mail == got_email.mail
    assert email.user_id == got_email.user_id


def test_delete_email(db: Session, email: EmailModel) -> None:
    got_email = emails_crud.delete(db=db, entity_id=email.id)
    assert got_email is not None
    assert email.id == got_email.id
    assert email.mail == got_email.mail
    assert email.user_id == got_email.user_id
