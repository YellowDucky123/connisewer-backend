from app.database import users, database
from flask import Flask, session, jsonify, request
from flask_jwt_extended import JWTManager
from flask_session import Session
from app import App
from hashlib import sha256

authUsers = database['authUsers']

# Setup Flask-Session (use server-side sessions)
App.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the filesystem
App.config['SECRET_KEY'] = 'your-secret-key'  # Secret key for session encryption

# Initialize Flask-JWT-Extended
App.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'  # Secret key for JWT encoding/decoding
jwt = JWTManager(App)

# return json
def authentication(email, password):
    userData = authUsers.find({"email": email})
    hashed_pass = sha256(password.encode('utf-8')).hexdigest()
    if hashed_pass == userData:
        user = users.find({"email": email})
         # Create a JWT token
        access_token = jwt.create_access_token(identity=user.name)
        session[access_token] = user._id
        
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
    access_token = jwt.create_access_token(identity=user['name'])
    session[access_token] = user['_id']

    return jsonify(access_token=access_token), 200

def userLogout(access_token):
    res = session.pop(access_token, None)
    if res is None:
        return jsonify(message="error: token does not exist"), 400
    return jsonify(message="logged out"), 200