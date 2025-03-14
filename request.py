from flask import Flask
from logic import toilet
from logic import user
from API import client

app = Flask(__name__)

database = client["test_database"]
collection_list = database.list_collections()

result = ""

for c in collection_list:
    result += "<p>" + c.get("name") + "</p>"

@app.route('/')
def hello():
    return result

def get_db():
    if app.config.get('TESTING'):
        return client['test_db']
    return client['catalyst']

#---------------------------------------------------------------------------------------#
#------------------------------------ USER ROUTES --------------------------------------#
#---------------------------------------------------------------------------------------#

@app.route('/', methods=['POST'])
def addUser():
    return user.addUser()

#---------------------------------------------------------------------------------------#
#------------------------------------ REVIEW ROUTES ------------------------------------#
#---------------------------------------------------------------------------------------#

@app.route('/', methods=['POST'])
def register():
    return user.register_user(get_db()) # function to register user

#---------------------------------------------------------------------------------------#
#------------------------------------ TOILET ROUTES ------------------------------------#
#---------------------------------------------------------------------------------------#

@app.route('/', methods=['POST'])
