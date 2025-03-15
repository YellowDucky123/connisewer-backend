from app.database import users, toilets
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
    return users.insert_one({"name": name, "email": email}).inserted_id
    

def delete(id):
    users.delete_one(id_query(id))

def post_review(user_id, toilet_id, text, value):
    review_id = review.create_review(user_id, toilet_id, text, value)
    rating_id = rating.create_rating(user_id, toilet_id, value) 
    users.update_one(id_query(user_id),
                     { "$push": { "reviews": review_id, "ratings": rating_id }})
    toilets.update_one(id_query(toilet_id),
                     { "$push": { "reviews": review_id, "ratings": rating_id }})
    
