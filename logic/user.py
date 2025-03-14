from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']
collection = database('toilet')

class User:
    def __init__(self, name, id):
        self.id = id
        self.name = name


def addUser(name, id):
    user = User(name, id)
    
