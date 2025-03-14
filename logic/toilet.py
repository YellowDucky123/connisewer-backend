from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']

class Toilet:
    def __init__(self, longitude, latitude, title, desc, rating, user):
        self.longitude = longitude  # Assigns input parameter to instance variable
        self.latitude = latitude
        self.title = title
        self.desc = desc
        self.rating = rating
        self.user = user

