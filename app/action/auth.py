from app.database import users, database, authUsers
from flask import Flask, session, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from app import App
from hashlib import sha256

# Setup Flask-Session (use server-side sessions)
jwt = JWTManager(App)

# Initialize Flask-Session

# return json
def authentication(email, password):
    userData = authUsers.find_one({"email": email})

    if not userData:
        return jsonify({"message": "User not found"}), 404

    hashed_pass = sha256(password.encode('utf-8')).hexdigest()

    if hashed_pass == userData["password"]:
        user = users.find_one({"email": email})

        if not user:
            return jsonify({"message": "User data not found"}), 404

        # Create a JWT token
        access_token = create_access_token(identity=user["name"])

        # Store user ID and email in session
        session["user_info"] = (str(user["_id"]), user["email"])  # Ensure _id is a string

        return jsonify(access_token=access_token), 200

    return jsonify({"message": "Invalid credentials"}), 401

def addNewUserData(email, password):
    hashed_pass = sha256(password.encode('utf-8')).hexdigest()
    authUsers.insert_one({
        "email": email,
        "password": hashed_pass
    })

def makeToken(email):
    user = users.find_one({"email": email})
    if not user:
        return "-1"
    access_token = create_access_token(identity=user['name'])

    # Store user ID and email in session as a tuple
    session['user_info'] = (user['_id'], user['email']) # userId is ObjectId() in this

    return access_token

def userLogout():
    res = session.pop('user_info', None)
    if res is None:
        return jsonify(message="error: token does not exist"), 400
    return jsonify(message="logged out"), 200
