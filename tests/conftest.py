import pytest
import server
from server import app


@pytest.fixture()
def list_compet():
    competitions = [{
            "name": "Spring Festival",
            "date": "2022-10-27 10:00:00",
            "number_of_places": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2010-10-22 13:30:00",
            "number_of_places": "13"
        }
    ]
    return competitions


@pytest.fixture()
def list_club():
    clubs = [
            {
                "name": "Simply Lift",
                "email": "john@simplylift.co",
                "points": "13"
            },
            {
                "name": "Iron Temple",
                "email": "admin@irontemple.com",
                "points": "4"
            },
            {
                "name": "She Lifts",
                "email": "kate@shelifts.co.uk",
                "points": "12"
            }
        ]
    return clubs


@pytest.fixture
def client(monkeypatch, list_club, list_compet):
    monkeypatch.setattr(server, 'clubs', list_club)
    monkeypatch.setattr(server, 'competitions', list_compet)
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
def club_user_2():
    cl = {
        "name": "She Lifts",
        "email": "kate@shelifts.co.uk",
        "points": "12"}
    return cl


@pytest.fixture
def compet():
    comp = {
            "name": "Spring Festival",
            "date": "2022-10-27 10:00:00",
            "number_of_places": "25"}
    return comp


@pytest.fixture
def past_compet():
    comp = {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "number_of_places": "13"}
    return comp
