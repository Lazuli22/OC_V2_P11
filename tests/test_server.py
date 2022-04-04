import pytest
from server import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def club_user():
    cl = {
        "name": "Simply Lift",
        "email": "john@simplylift.co",
        "points": "13"}
    return cl


@pytest.fixture
def compet():
    comp = {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "number_of_places": "25"}
    return comp


# fixture pour charger les données
def test_login_user_invalid_credentials(client):
    """
    GIVEN a flask application configured for testing
    WHEN the page '/show_summary' is posted (POST) with invalid credentials
    THEN check the same page  with a wrong message
    """
    response = client.post('/show_summary', data={'email': 'abc@gmail.com'})
    assert response.status_code == 200
    assert b"Utilisateur non reconnu" in response.data


def test_valid_credentials(client):
    """
    GIVEN a flask application configured for testing
    WHEN the page '/show_summary' is requested (POST) with valid credentials
    THEN check a page  with valid message
    """
    response = client.post('/show_summary', data={'email': 'john@simplylift.co'})
    print(response)
    assert response.status_code == 200
    assert b"Welcome, john@simplylift.co" in response.data


def test_empty_credentials(client):
    """
    GIVEN a flask application configured for testing
    WHEN the page '/show_summary' is requested (POST) with empty credentials
    THEN check the same page  with a warning message
    """
    response = client.post('/show_summary', data={'email': ''})
    assert response.status_code == 200
    assert b"Email vide" in response.data


def test_correct_points_allowed_per_clubs(client, club_user, compet):
    """
    GIVEN a club authentified
    WHEN club books a number of places for a competition
    THEN check the booking doesn't exceed points of the club
    """
    place = "15"
    response = client.post(
                '/purchase_places',
                data={
                    'club': club_user['name'],
                    'competition': compet['name'],
                    'points': club_user['points'],
                    'places': place}
            )
    assert response.status_code == 200
    assert b'Ce club n a pas assez de points pour reserver' in response.data
