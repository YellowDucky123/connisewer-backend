from flask import Flask
from flask_session import Session

App = Flask(__name__)

App.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the filesystem
App.config['SECRET_KEY'] = 'your-secret-key'  # Secret key for session encryption
App.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key'  # Secret key for JWT encoding/decoding

Session(App)

import app.routes
