<<<<<<< HEAD
from app.database import users, toilets, reviews
=======
from app.database import users, toilets, authUsers
>>>>>>> c0503ed (added comments)
from flask import jsonify
from app.utils import id_query
from bson import ObjectId
from . import review, rating, auth

def find_by_email(email):
    return users.find_one({ "email": email })

def find_by_name(name):
    return users.find_one({ "name": name })

def find_by_id(id):
    return users.find_one(id_query(id))

def register(name, email, password):
    auth.addNewUserData(email, password)
    users.insert_one({"name": name, "email": email}).inserted_id
    token = auth.makeToken(email)
    if token == '-1':
        return jsonify(message='registration failed'), 400
    return jsonify(access_token=token), 200

def get_reviews(id):
    return reviews.find({ "user": id} ).limit(20)
    

def delete(id):
    userEmail = users.find(id_query(id))['email']
    authUsers.delete_one({"email": userEmail})
    users.delete_one(id_query(id))

def post_review(user_id, toilet_id, text, value):
    review_id = review.create_review(user_id, toilet_id, text, value)
    rating_id = rating.create_rating(user_id, toilet_id, value) 
    users.update_one(id_query(user_id),
                     { "$push": { "reviews": review_id, "ratings": rating_id }})
    toilets.update_one(id_query(toilet_id),
                     { "$push": { "reviews": review_id, "ratings": rating_id }})
    
def remove_review(review_id):
    review.delete_review(review_id)

def change_review(review_id, text, rating):
    rev = review.update_one({"_id": review_id}, { "text": text, "rating": rating})
    if rev == 0:
        return jsonify(message="change failed to process"), 400
    return jsonify(message="review changed/updated"), 200

