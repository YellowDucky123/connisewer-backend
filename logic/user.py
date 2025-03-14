from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']

class User:
    def __init__(self, name):
        self.name = name


def addUser(name):
    user = User(name)