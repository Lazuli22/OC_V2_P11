


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
    assert b'this club doesn t have enought points for booking' in response.data


# Définition d'un 2nd test pour le bug n°2
def test_update_points(client, compet, club_user):
    """
    GIVEN a club authentified
    WHEN club books a number of places for a competition
    THEN check the booking subtracts the number of places on user's points
    """
    place = "10"
    initial_points = int(club_user["points"])
    print(initial_points)
    response = client.post(
                '/purchase_places',
                data={
                    'club': club_user['name'],
                    'competition': compet['name'],
                    'points': club_user['points'],
                    'places': place}
            )
    assert response.status_code == 200
    assert b'Points available: 3' in response.data


def test_books_limited_12points(client, compet, club_user):
    """
    GIVEN a club authentified
    WHEN club books a number of places for a competition
    THEN check  the number of booked places is under 12 
    """
    place = "13"
    initial_points = int(club_user["points"])
    print(initial_points)
    response = client.post(
                '/purchase_places',
                data={
                    'club': club_user['name'],
                    'competition': compet['name'],
                    'points': club_user['points'],
                    'places': place}
            )
    assert response.status_code == 200
    assert b'You can t book over 12 points' in response.data
 