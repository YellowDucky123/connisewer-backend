from flask import Flask
from app.database import client

app = Flask(__name__)

database = client['connisewer']
collection = database['toilets']


class Toilet:
    def __init__(self, id, longitude, latitude, title, desc, rating, user):
        self._id = id
        self.location = {longitude, latitude}
        self.title = title
        self.desc = desc
        self.rating = rating
        self.user = user

