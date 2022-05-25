from locust import HttpUser, task


class ProjectPerfTest(HttpUser):

    @task()
    def competitions_page(self):
        with self.client.post(
            "http://127.0.0.1:5000/show_summary",
            {"email": "john@simplylift.co"}, catch_response=True
        ) as response:
            if b"Welcome, john@simplylift.co" not in response.content:
                response.failure(" invalide email!")
            elif response.elapsed.total_seconds() > 5:
                response.failure("Request takes too long")

    @task()
    def book_competition_page(self):
        with self.client.post(
            'http://127.0.0.1:5000/purchase_places',
            {"club": 'She Lifts', 'competition': 'Spring Festival',
                'points': '12', 'places': 10},
                catch_response=True
        ) as response:
            if response.elapsed.total_seconds() > 2:
                response.failure("Request takes too long")

