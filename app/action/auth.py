from app.database import users, database, authUsers
from flask import Flask, session, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from app import App
from hashlib import sha256

# Setup Flask-Session (use server-side sessions)
jwt = JWTManager(App)

# return json
def authentication(email, password):
    # Find the user in the authentication database
    userData = authUsers.find_one({"email": email})

    if not userData:
        return jsonify({"message": "User not found"}), 404

    # Hash the input password for comparison
    hashed_pass = sha256(password.encode('utf-8')).hexdigest()

    if hashed_pass == userData["password"]:  # Password matches
        user = users.find_one({"email": email})  # Get user details

        if not user:
            return jsonify({"message": "User data not found"}), 404

        # Generate JWT token
        token = makeToken(email)

        if token == '-1':  # Token generation failed
            return jsonify(message='Invalid credentials'), 400

        return jsonify(access_token=token), 200

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
