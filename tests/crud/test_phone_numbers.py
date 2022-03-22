from sqlalchemy.orm import Session

from app.crud.phone_numbers import phone_numbers_crud
from app.models.phone_numbers import PhoneNumbers as PhoneNumberModel


def test_create_phone_numbers(db: Session, phone_number_dict: dict) -> None:
    phone_number = phone_numbers_crud.create(db=db, obj_in=phone_number_dict)
    assert phone_number_dict.get("number", None) == phone_number.number
    assert phone_number_dict.get("user_id", None) == phone_number.user_id


def test_read_phone_numbers(
    db: Session, phone_number: PhoneNumberModel
) -> None:
    phone_numbers = phone_numbers_crud.read_many(db=db)
    for phone_number in phone_numbers:
        assert isinstance(phone_number, PhoneNumberModel)


def test_read_phone_number(
    db: Session, phone_number: PhoneNumberModel
) -> None:
    got_phone_number = phone_numbers_crud.read(
        db=db, entity_id=phone_number.id
    )
    assert got_phone_number is not None
    assert phone_number.id == got_phone_number.id
    assert phone_number.number == got_phone_number.number
    assert phone_number.user_id == got_phone_number.user_id


def test_update_phone_number(
    db: Session, phone_number: PhoneNumberModel, phone_number_dict: dict
) -> None:
    got_phone_number = phone_numbers_crud.update(
        db=db, db_obj=phone_number, obj_in=phone_number_dict
    )
    assert phone_number.id == got_phone_number.id
    assert phone_number.number == got_phone_number.number
    assert phone_number.user_id == got_phone_number.user_id


def test_delete_phone_number(
    db: Session, phone_number: PhoneNumberModel
) -> None:
    got_phone_number = phone_numbers_crud.delete(
        db=db, entity_id=phone_number.id
    )
    assert got_phone_number is not None
    assert phone_number.id == got_phone_number.id
    assert phone_number.number == got_phone_number.number
    assert phone_number.user_id == got_phone_number.user_id
