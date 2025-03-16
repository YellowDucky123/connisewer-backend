from flask import Flask
from flask_session import Session

App = Flask(__name__)

App.config["SESSION_PERMANENT"] = False
App.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the filesystem
Session(App)

import app.routes
