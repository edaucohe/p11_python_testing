from urllib.parse import quote
from locust import HttpUser, task, between


class WebsitePerformance(HttpUser):
    wait_time = between(1, 5)
    club = {
        "name": "Iron Temple",
        "email": "admin@irontemple.com",
        "points": "4"
    }
    competition = {
        "name": "Spring Festival",
        "date": "2020-03-27 10:00:00",
        "numberOfPlaces": "25"
    }

    @task
    def index(self):
        self.client.get(url="/")

    @task
    def login(self):
        data = {
            "email": self.club["email"]
        }
        self.client.post(url='/showSummary', data=data)

    @task
    def booking(self):
        competition_name = quote(self.competition["name"])
        club_name = quote(self.club["name"])
        self.client.get(url=f'/book/{competition_name}/{club_name}')

    @task
    def purchase_places(self):
        data = {
            "club": self.club["name"],
            "competition": self.competition["name"],
            "places": 2
        }
        self.client.post(url='/purchasePlaces', data=data)

    @task
    def display_clubs(self):
        self.client.get(url="/clubs")
