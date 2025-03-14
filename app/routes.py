from . import App
from bson import json_util
from .logic import toilet
from .logic import user
import json
from .database import client, database


toilets = database['toilets']

result = ""

for c in toilets.find():
    result += "<p>" + c.get("title") + "</p>"

@App.route('/')
def hello():
    return result

@App.route("/toilets/search=<query>", methods=['GET'])
def search(query):
    curs = toilets.find({ "title": {"$regex": query}})
    return json.loads(json_util.dumps(curs))
    
database = client["test_database"]
collection_list = database.list_collections()

result = ""

for c in collection_list:
    result += "<p>" + c.get("name") + "</p>"
# this might not be used in this
def get_db():
    if App.config.get('TESTING'):
        return client['test_db']
    return client['catalyst']

def toJSON(thing):
    return json.loads(json.dumps(thing))

#---------------------------------------------------------------------------------------#
#------------------------------------ USER ROUTES --------------------------------------#
#---------------------------------------------------------------------------------------#

# add a user
@App.route('/user/add/name=<name>/email=<email>/', methods=['POST'])
def registerUser(name, email):
    return toJSON(user.addUser(name, None, email))

# # delete a user
# @App.route('/', methods=['DELETE'])
# def deleteUser():
#
#
#
# #---------------------------------------------------------------------------------------#
# #------------------------------------ REVIEW ROUTES ------------------------------------#
# #---------------------------------------------------------------------------------------#
#
# # user makes a review
# @App.route('/', methods=['POST'])
# def makeReview(userId):
#     
#
# # user deletes a review
# @App.route('/', methods=['DELETE'])
# def u
#
#
# #---------------------------------------------------------------------------------------#
# #------------------------------------ TOILET ROUTES ------------------------------------#
# #---------------------------------------------------------------------------------------#
#
# @App.route('/', methods=['POST'])
