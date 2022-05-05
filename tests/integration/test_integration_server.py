"""
Integration tests for the server.py file
"""
from flask import session


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


