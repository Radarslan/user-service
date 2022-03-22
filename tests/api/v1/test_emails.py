from starlette.testclient import TestClient

from app.core.settings import settings
from app.models.emails import Emails as EmailModel
from app.models.users import Users as UserModel
from app.schemas.v1.email import Email
from tests.utils.assertions import assert_unique_violation


def test_create_emails(
    test_client: TestClient, user: UserModel, email_dict: dict
) -> None:
    response = test_client.post(
        f"{settings.API_VERSION}/users/{user.id}/emails/", json=email_dict
    )
    response_body = response.json()
    if response.status_code == 400:
        assert_unique_violation(response_body, email_dict.get("mail"))
    else:
        assert response.status_code == 201
        assert email_dict.get("mail", None) == response_body.get("mail", None)
        assert email_dict.get("user_id", None) == response_body.get(
            "user_id", None
        )


def test_read_emails(
    test_client: TestClient, user: UserModel, email: EmailModel
) -> None:
    response = test_client.get(
        url=f"{settings.API_VERSION}/users/{user.id}/emails/"
    )
    assert response.status_code == 200
    for email in response.json():
        Email(**email)


def test_read_email(
    test_client: TestClient, user: UserModel, email: EmailModel
) -> None:
    response = test_client.get(
        f"{settings.API_VERSION}/users/{user.id}/emails/{email.id}"
    )
    got_email = response.json()
    assert response.status_code == 200
    assert email.id == got_email.get("id", None)
    assert email.mail == got_email.get("mail", None)
    assert email.user_id == got_email.get("user_id", None)


def test_update_email(
    test_client: TestClient,
    user: UserModel,
    email: EmailModel,
    email_dict: dict,
) -> None:
    response = test_client.put(
        f"{settings.API_VERSION}/users/{user.id}/emails/{email.id}",
        json=email_dict,
    )
    response_body = response.json()
    if response.status_code == 400:
        assert_unique_violation(response_body, email_dict.get("mail"))
    else:
        assert response.status_code == 200
        assert email.id == response_body.get("id", None)
        assert email.mail == response_body.get("mail", None)
        assert email.user_id == response_body.get("user_id", None)


def test_delete_email(
    test_client: TestClient, user: UserModel, email: EmailModel
) -> None:
    response = test_client.delete(
        f"{settings.API_VERSION}/users/{user.id}/emails/{email.id}"
    )
    got_email = response.json()
    assert response.status_code == 200
    assert email.id == got_email.get("id", None)
    assert email.mail == got_email.get("mail", None)
    assert email.user_id == got_email.get("user_id", None)
