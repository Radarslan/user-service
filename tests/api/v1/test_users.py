from starlette.testclient import TestClient

from app.core.settings import settings
from app.models.users import Users as UserModel
from app.schemas.v1.user import User
from tests.utils.assertions import assert_unique_violation


def test_create_users(test_client: TestClient, user_dict: dict) -> None:
    response = test_client.post(
        f"{settings.API_VERSION}/users/", json=user_dict
    )
    response_body = response.json()
    if response.status_code == 400:
        assert_unique_violation(response_body, user_dict.get("emails")[0])
        assert_unique_violation(
            response_body, user_dict.get("phone_numbers")[0]
        )
    else:
        assert response.status_code == 201
        assert user_dict.get("first_name", None) == response_body.get(
            "first_name", None
        )
        assert user_dict.get("last_name", None) == response_body.get(
            "last_name", None
        )
        assert user_dict.get("emails", None) == response_body.get(
            "phone_number", None
        )
        assert user_dict.get("phone_numbers", None) == response_body.get(
            "phone_numbers", None
        )
        assert user_dict.get("is_active", None) == response_body.get(
            "is_active", None
        )


def test_find_users(test_client: TestClient, user: UserModel) -> None:
    params = {
        "first_name": user.first_name[1:3],
        "last_name": user.last_name[1:3],
        "is_active": user.is_active,
    }
    response = test_client.get(
        url=f"{settings.API_VERSION}/users/", params=params
    )
    assert response.status_code == 200
    for got_user in response.json():
        User(**got_user)
        assert (
            user.first_name[1:3] in got_user.first_name
            and user.last_name[1:3] in got_user.last_name
            and user.is_active == got_user.is_active
        )


def test_read_user(test_client: TestClient, user: UserModel) -> None:
    response = test_client.get(f"{settings.API_VERSION}/users/{user.id}")
    got_user = response.json()
    assert response.status_code == 200
    assert user.id == got_user.get("id", None)
    assert user.first_name == got_user.get("first_name", None)
    assert user.last_name == got_user.get("last_name", None)
    assert user.emails == got_user.get("emails", None)
    assert user.phone_numbers == got_user.get("phone_numbers", None)
    assert user.is_active == got_user.get("is_active", None)


def test_update_user(
    test_client: TestClient, user: UserModel, user_dict: dict
) -> None:
    del user_dict["wallet_balance"]
    response = test_client.put(
        f"{settings.API_VERSION}/users/{user.id}",
        json=user_dict,
    )
    got_user = response.json()
    assert response.status_code == 200
    assert user.id == got_user.get("id", None)
    assert user.first_name == got_user.get("first_name", None)
    assert user.last_name == got_user.get("last_name", None)
    assert user.emails == got_user.get("emails", None)
    assert user.phone_numbers == got_user.get("phone_numbers", None)
    assert user.is_active == got_user.get("is_active", None)


def test_delete_user(test_client: TestClient, user: UserModel) -> None:
    response = test_client.delete(f"{settings.API_VERSION}/users/{user.id}")
    got_user = response.json()
    assert response.status_code == 200
    assert user.id == got_user.get("id", None)
    assert user.first_name == got_user.get("first_name", None)
    assert user.last_name == got_user.get("last_name", None)
    assert user.emails == got_user.get("emails", None)
    assert user.phone_numbers == got_user.get("phone_numbers", None)
    assert user.is_active != got_user.get("is_active", None)
