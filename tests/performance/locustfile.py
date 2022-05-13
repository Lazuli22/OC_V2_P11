from urllib import response
from locust import HttpUser, task, between


class ProjectPerfTest(HttpUser):

    @task
    def home(self):
        self.client.get("/")

    @task()
    def competitions_page(self):
        self.client.post(
            "http://127.0.0.1:5000/show_summary",
            {"email": "john@simplylift.co"}, catch_response=True) 
            as response: 
                if not b"Welcome to the GUDLFT" in response.data
                    response.failure("email invalide!")

    @task()
    def book_competition_page(self, club_user_2, compet):
        between(5, 9)
        self.client.post(
            'http://127.0.0.1:5000/purchase_places',
            {"club": club_user_2['name'], 'competition': compet['name'],
                'points': club_user_2['points'], 'places': 10}
        )
