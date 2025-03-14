from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']
collection = database['toilets']

class User:
    # name = string
    # id = string
    # email = string
    # profile_pic = ????
    # reviews = array
    # ratings = array
    def __init__(self, name, id, profile_pic, email, reviews, ratings):
        self.id = id
        self.name = name
        self.profile_pic = profile_pic
        self.email = email
        self.arrayReviews = reviews
        self.arrayRatings = ratings


# add user
def addUser(name, id, profile_pic, email, reviews, ratings):
    user = User(name, id, profile_pic, email, reviews, ratings) # make user
    collection.insert_one(user.to_dict())   # add user to collection/database

    
