from app.database import database
from bson import ObjectId

users = database['users']

def find_by_email(email):
    return users.find_one({ "email": email })

def find_by_name(name):
    return users.find_one({ "name": name })

def find_by_id(id):
    return users.find_one({ "_id": ObjectId(id) })

def register(name, email):
    out = users.insert_one({"name": name, "email": email})
    print(out.__inserted_id)
    return out

def delete(id):
    users.delete_one({ "_id": ObjectId(id)})


