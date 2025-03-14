from .review import Review
from bson import ObjectId
from datetime import datetime

from app.database import database

collection = database['user']

class User:
    # name = string
    # id = string
    # email = string
    # profile_pic = ????
    # reviews = array (dictionary)
    # ratings = array (dictionary)
    def __init__(self, name, id, profile_pic, email, reviews, ratings):
        self._id = id
        self.name = name
        self.profile_pic = profile_pic
        self.email = email
        self.dictReviews = reviews
        self.dictRatings = ratings  
    
    def to_dict(self):
        return {
        "_id": str(self._id),
        "name": self.name,
        "profile_pic": self.profile_pic,
        "email": self.email,
        "dictReviews": self.dictReviews,
        "dictRatings": self.dictRatings }


# add user
def addUser(name, profile_pic, email):
    user = User(name, ObjectId(), profile_pic, email, {}, {}).to_dict() # make user
    collection.insert_one(user)   # add user to collection/database
    return user

# delete user
def deleteUser(userId):
    query = { "_id": ObjectId(userId) }
    return collection.delete_one(query)   
    
