from BSON import ObjectId
from datetime import datetime


from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']
collection = database['reviews']

class Review: 
    def __init__(self, id, name, text, date):
        self._id = id
        self.userId = name
        self.text = text
        self.date = date


# add review
    def addReview(self, userId, text):
        query = { "_id": ObjectId(userId) }
        user = database.user.find(query)
        date = datetime.now()  # Use current date
        review = Review(ObjectId(), user.name, text, date)
        user.arrayReviews.append(review.to_dict())  # Add review to the reviews array
        collection.insert_one(review.to_dict()) # add to database
        collection.update_one(query, user)  # update the user array
        return review

    # deleting a review
    def deleteReview(self, reviewId):
        query = { "_id": ObjectId(reviewId) }
        return collection.delete_one(query)      