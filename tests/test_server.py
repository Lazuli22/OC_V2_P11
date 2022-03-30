import pytest
from server import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client


def test_login_user_invalid_credentials(client):
    """ this test demontrates that a connexion with wrong identifiants
    shows the same page with a wong message"""
    response = client.post('/show_summary', data={'email': 'abc@gmail.com'})
    assert b"Utilisateur non reconnu" in response.data


def test_valid_credentials(client):
    response = client.post('/show_summary', data={'email': 'john@simplylift.co'})
    print(response)
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data


def test_empty_credentials(client):
    """ this test demontrates that a connexion with empty identifiants
    shows the same page with a warning message"""
    response = client.post('/show_summary', data={'email': ''})
    assert b"Email vide" in response.data
