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

# this might not be used in this
def get_db():
    if app.config.get('TESTING'):
        return client['test_db']
    return client['catalyst']

#---------------------------------------------------------------------------------------#
#------------------------------------ USER ROUTES --------------------------------------#
#---------------------------------------------------------------------------------------#

# add a user
@app.route('/', methods=['POST'])
def addUser():
    return user.addUser(insert name, insert id)

# delete a user
@app.route('/', methods=['DELETE'])
def deleteUser():



#---------------------------------------------------------------------------------------#
#------------------------------------ REVIEW ROUTES ------------------------------------#
#---------------------------------------------------------------------------------------#

# user makes a review
@app.route('/', methods=['POST'])
def makeReview(userId):
    

# user deletes a review
@app.route('/', methods=['DELETE'])
def u


#---------------------------------------------------------------------------------------#
#------------------------------------ TOILET ROUTES ------------------------------------#
#---------------------------------------------------------------------------------------#

@app.route('/', methods=['POST'])
