from starlette.testclient import TestClient

from app.core.settings import settings
from app.models.phone_numbers import PhoneNumbers as PhoneNumberModel
from app.models.users import Users as UserModel
from app.schemas.v1.phone_number import PhoneNumber
from tests.utils.assertions import assert_unique_violation


def test_create_phone_numbers(
    test_client: TestClient, user: UserModel, phone_number_dict: dict
) -> None:
    response = test_client.post(
        f"{settings.API_VERSION}/users/{user.id}/phone_numbers/",
        json=phone_number_dict,
    )
    response_body = response.json()
    if response.status_code == 400:
        assert_unique_violation(response_body, phone_number_dict.get("number"))
    else:
        assert response.status_code == 201
        assert phone_number_dict.get("number", None) == response_body.get(
            "number", None
        )
        assert phone_number_dict.get("user_id", None) == response_body.get(
            "user_id", None
        )


def test_read_phone_numbers(
    test_client: TestClient, user: UserModel, phone_number: PhoneNumberModel
) -> None:
    response = test_client.get(
        url=f"{settings.API_VERSION}/users/{user.id}/phone_numbers/"
    )
    assert response.status_code == 200
    for phone_number in response.json():
        PhoneNumber(**phone_number)


def test_read_phone_number(
    test_client: TestClient, user: UserModel, phone_number: PhoneNumberModel
) -> None:
    response = test_client.get(
        f"{settings.API_VERSION}/users/{user.id}"
        f"/phone_numbers/{phone_number.id}"
    )
    got_phone_number = response.json()
    assert response.status_code == 200
    assert phone_number.id == got_phone_number.get("id", None)
    assert phone_number.number == got_phone_number.get("number", None)
    assert phone_number.user_id == got_phone_number.get("user_id", None)


def test_update_phone_number(
    test_client: TestClient,
    user: UserModel,
    phone_number: PhoneNumberModel,
    phone_number_dict: dict,
) -> None:
    response = test_client.put(
        f"{settings.API_VERSION}/users/{user.id}"
        f"/phone_numbers/{phone_number.id}",
        json=phone_number_dict,
    )
    response_body = response.json()
    if response.status_code == 400:
        assert_unique_violation(response_body, phone_number_dict.get("number"))
    else:
        assert response.status_code == 200
        assert phone_number.id == response_body.get("id", None)
        assert phone_number.number == response_body.get("number", None)
        assert phone_number.user_id == response_body.get("user_id", None)


def test_delete_phone_number(
    test_client: TestClient, user: UserModel, phone_number: PhoneNumberModel
) -> None:
    response = test_client.delete(
        f"{settings.API_VERSION}/users/{user.id}"
        f"/phone_numbers/{phone_number.id}"
    )
    got_phone_number = response.json()
    assert response.status_code == 200
    assert phone_number.id == got_phone_number.get("id", None)
    assert phone_number.number == got_phone_number.get("number", None)
    assert phone_number.user_id == got_phone_number.get("user_id", None)
