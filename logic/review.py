from BSON import ObjectId
from datetime import datetime


from flask import Flask
from API import client

app = Flask(__name__)

database = client['connisewer']
collection = database['reviews']
userCollection = database.user

class Review: 
    def __init__(self, id, name, text, date):
        self._id = id
        self.userId = name
        self.text = text
        self.date = date


# add review
    def addReview(self, userId, text):
        query = { "_id": ObjectId(userId) }
        
        user = userCollection.find(query)

        date = datetime.now()  # Use current date

        review = Review(ObjectId(), user.name, text, date).to_dict() # make the review

        user.dictReviews[review._id] = review  # Add review to the "reviews array"

        collection.insert_one(review) # add to "review database"

        userCollection.update_one(query, user)  # update the user array in the "user database"

        return review

    # deleting a review
    def deleteReview(self, userId, reviewId):
        queryUser = { "_id": ObjectId(userId) }

        queryReview = { "_id": ObjectId(reviewId) }

        user = database.user.find(queryUser)

        # delete the review in the user array
        user.dictReviews.pop(reviewId)

        return collection.delete_one(queryReview)      