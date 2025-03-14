from app.database import database
from app.utils import id_query
from bson import ObjectId
from . import review

users = database['users']

def find_by_email(email):
    return users.find_one({ "email": email })

def find_by_name(name):
    return users.find_one({ "name": name })

def find_by_id(id):
    return users.find_one(id_query(id))

def register(name, email):
    return users.insert_one({"name": name, "email": email})
    

def delete(id):
    users.delete_one(id_query(id))

def post_review(user_id, toilet_id, text):
    result = review.create_review(user_id, toilet_id, text)
    review_id = result.inserted_id
    users.update_one(id_query(user_id),
                     { "$push": { "reviews": review_id }})
    
