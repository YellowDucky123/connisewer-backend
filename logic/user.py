from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']
collection = database['toilets']

class User:
    def __init__(self, name, id):
        self.id = id
        self.name = name


# add user
def addUser(name, id):
    user = User(name, id)
    collection.insert_one(user.to_dict())

    
