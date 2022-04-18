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


@pytest.fixture
def past_compet():
    comp = {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "number_of_places": "13"}
    return comp
