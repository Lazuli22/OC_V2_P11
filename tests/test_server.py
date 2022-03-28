import pytest
from server import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_login_user_invalid_credentials(client):
    response = client.post(
        '/',
        data=dict(email="abc@gmail.com", password="password"),
        follow_redirects=True,
        )
    assert b"Utisateur non enregistre" in response.data
