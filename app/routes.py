from . import App
from bson import json_util
from .action import user
import json
from .database import client, database
from flask import request


toilets = database['toilets']

result = ""

for c in toilets.find():
    result += "<p>" + c.get("title") + "</p>"

@App.route('/')
def hello():
    return result

@App.route("/toilets/search=<query>", methods=['GET'])
def search(query):
    print("aaa")
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
    return json.loads(json_util.dumps(thing))

#---------------------------------------------------------------------------------------#
#------------------------------------ USER ROUTES --------------------------------------#
#---------------------------------------------------------------------------------------#

# add a user
@App.route('/user/add/name=<name>/email=<email>', methods=['POST'])
def registerUser(name, email):
    user.register(name, email)
    return "success"

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
# user makes a review
@App.route('/user/post-review', methods=['POST'])
def makeReview():
    user_id = request.args["user_id"]
    toilet_id = request.args["toilet_id"]
    text = request.args["text"]
    user.post_review(user_id, toilet_id, text)
    return "success"


    
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
