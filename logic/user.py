from .review import Review
from BSON import ObjectId
from datetime import datetime

from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']
collection = database['user']

class User:
    # name = string
    # id = string
    # email = string
    # profile_pic = ????
    # reviews = array
    # ratings = array
    def __init__(self, name, id, profile_pic, email, reviews, ratings):
        self._id = id
        self.name = name
        self.profile_pic = profile_pic
        self.email = email
        self.arrayReviews = reviews
        self.arrayRatings = ratings  

# add user
def addUser(name, profile_pic, email, reviews, ratings):
    user = User(name, ObjectId(), profile_pic, email, reviews, ratings) # make user
    collection.insert_one(user.to_dict())   # add user to collection/database
    return user

# delete user
def deleteUser(userId):
    query = { "_id": ObjectId(userId) }
    return collection.delete_one(query)   
    
