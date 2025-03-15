from app.database import users, database, authUsers
from flask import Flask, session, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from flask_session import Session
from app import App
from hashlib import sha256

# Setup Flask-Session (use server-side sessions)
App.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the filesystem
App.config['SECRET_KEY'] = 'your-secret-key'  # Secret key for session encryption

# Initialize Flask-JWT-Extended
App.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'  # Secret key for JWT encoding/decoding
jwt = JWTManager(App)

# Initialize Flask-Session
Session(App)

# return json
def authentication(email, password):
    userData = authUsers.find_one({"email": email})
    hashed_pass = sha256(password.encode('utf-8')).hexdigest()

    # checks if the password is right
    if hashed_pass == userData['password']:
        user = users.find_one({"email": email})

         # Create a JWT token
        access_token = create_access_token(identity=user['name'])

        # Store user ID and email in session as a tuple
        session['user_info'] = (user['_id'], user['email']) # userId is ObjectId() in this
        
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401

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