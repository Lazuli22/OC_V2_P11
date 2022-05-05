"""
Integration tests for the server.py file
"""


def test_login_route(client):

    credentials = {
        'email': 'john@simplylift.co'
    }
    response = client.post('/show_summary', data=credentials)
    assert response.status_code == 200
    assert response.request.path == '/show_summary'
    assert b'Welcome, john@simplylift.co ' in response.data
    response_logout = client.get('/logout', follow_redirects=True)
    assert response_logout.request.path == "/"
    assert response_logout.status_code == 200
    assert b'Welcome to the GUDLFT Registration Portal!' in response_logout.data


def test_booking_route(client, club_user_2, compet):
    my_data = {
            'club': club_user_2['name'],
            'competition': compet['name'],
            'points': club_user_2['points'],
            'places': 10
            }
    res = client.post(
                '/purchase_places',
                data=my_data
            )
    assert res.status_code == 200
    assert b'Welcome, kate@shelifts.co.uk' in res.data
    assert b'Points available: 2' in res.data
    assert b'Number of Places: 15' in res.data


def test_limite_booking_route(client, club_user, compet):
    my_data = {
        'club': club_user['name'],
        'competition': compet['name'],
        'points': club_user['points'],
        'places': 13
        }
    res = client.post(
                '/purchase_places',
                data=my_data
            )
    assert res.status_code == 200
    assert b'Welcome, john@simplylift.co' in res.data
    assert b'You can t book over 12 points' in res.data
    assert b'Points available: 1' in res.data
    assert b'Number of Places: 3' in res.data



