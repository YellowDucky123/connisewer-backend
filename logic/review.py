from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']

class Review: 
    def __init__(self, id, name, text, date):
        self.id = id
        self.userId = name
        self.text = text
        self.date = date
    