"""
Units tests for the server.py file
"""

from datetime import datetime


class TestsUnitServer:

    def test_global_view_clubs(self, client):
        """
        GIVEN a flask application configured for testing
        WHEN the page 'index.html' is requested
        THEN check the welcome page contains a points display board.
        """  
        response = client.get('/')
        assert response.status_code == 200
        assert b'Simply Lift' in response.data
        assert b'john@simplylift.co' in response.data
        assert b'1' in response.data
        assert b'Iron Temple' in response.data
        assert b'admin@irontemple.com' in response.data
        assert b'4' in response.data
        assert b'She Lifts' in response.data
        assert b'kate@shelifts.co.uk' in response.data
        assert b'2' in response.data

    def test_login_user_invalid_credentials(self, client):
        """
        GIVEN a flask application configured for testing
        WHEN the page '/show_summary' is posted (POST) with invalid credentials
        THEN check the same page  with a wrong message
        """
        response = client.post('/show_summary', data={'email': 'abc@gmail.com'})
        assert response.status_code == 200
        assert b"Welcome to the GUDLFT" in response.data
        assert b"Unknown user" in response.data

    def test_valid_credentials(self, client):
        """
        GIVEN a flask application configured for testing
        WHEN the page '/show_summary' is requested (POST) with valid credentials
        THEN check a page  with valid message
        """
        response = client.post(
                            '/show_summary',
                            data={'email': 'john@simplylift.co'}
                            )
        assert response.status_code == 200
        assert b"Welcome, john@simplylift.co" in response.data
        assert b'Logout' in response.data

    def test_empty_credentials(self, client):
        """
        GIVEN a flask application configured for testing
        WHEN the page '/show_summary' is requested (POST) with empty credentials
        THEN check the same page  with a warning message
        """
        response = client.post('/show_summary', data={'email': ''})
        assert response.status_code == 200
        assert b"Welcome to the GUDLFT" in response.data
        assert b"Empty Email" in response.data

    def test_correct_points_allowed_per_clubs(self, client, club_user, compet):
        """
        GIVEN a club authentified
        WHEN club books a number of places for a competition
        THEN check the booking doesn't exceed points of the club
        """
        place = "15"
        res = client.post(
                    '/purchase_places',
                    data={
                        'club': club_user['name'],
                        'competition': compet['name'],
                        'points': club_user['points'],
                        'places': place}
                )
        assert res.status_code == 200
        assert b"Welcome, john@simplylift.co" in res.data
        assert b'this club doesn t have enought points for booking' in res.data
        assert b'Logout' in res.data

    def test_books_limited_12points(self, client, compet, club_user):
        """
        GIVEN a club authentified
        WHEN club books a number of places for a competition
        THEN check  the number of booked places is under 12
        """
        place = "13"
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
        assert b'Points available: 1' in response.data
        assert b'Great-booking complete!' in response.data
        assert b'you have not enought points for booking' not in response.data
        assert b'Logout' in response.data

    def test_booking_past_competitions(self, client, past_compet, club_user):
        """
        GIVEN a club authentified, John Simplylift
        WHEN club books  places for a past competition, Fall Classic
        THEN check the booking can't done for a past competition.
        """
        response = client.get(
                    '/book/Fall Classic/Simply Lift',
                    data={
                        'club': club_user['name'],
                        'competition': past_compet['name'],
                        'points': club_user['points'],
                        }
                )
        the_actual_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        assert response.status_code == 200
        assert b"Welcome, john@simplylift.co" in response.data
        assert past_compet['date'] < the_actual_date
        assert b'You can t book a past competition' in response.data
        assert b'Logout' in response.data

    def test_booking_current_competitions(self, client, compet, club_user):
        """
        GIVEN a club authentified, John Simplylift
        WHEN club books  places for a current competition, Spring Festival
        THEN check the booking can be done for this competition.
        """
        response = client.get(
                    '/book/Spring Festival/Simply Lift',
                    data={
                        'club': club_user['name'],
                        'competition': compet['name'],
                        'points': club_user['points'],
                        }
                )
        the_actual_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        assert response.status_code == 200
        assert b"Spring Festival" in response.data
        assert compet['date'] > the_actual_date
        assert b'Places available' in response.data
        assert b'How many places?' in response.data

    def test_update_points(self, client, compet, club_user):
        """
        GIVEN a club authentified, John Simplylift
        WHEN the club books places for a current competition
        THEN check the club's points is updated
        """
        place = "10"
        response = client.post(
                    '/purchase_places',
                    data={
                        'club': club_user['name'],
                        'competition': compet['name'],
                        'points': club_user['points'],
                        'places': place}
                )
        assert response.status_code == 200
        assert b"Welcome, john@simplylift.co" in response.data
        assert b'Points available: 3' in response.data
        assert b'Logout' in response.data
