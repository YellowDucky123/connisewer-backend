from . import App
from .action import user
from .action import toilet
from .database import client, database
from flask import request
from .utils import to_json


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
    return to_json(curs)
    
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
    rating = int(request.args["rating"])
    user.post_review(user_id, toilet_id, text, rating)
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
@App.route('/toilets/minLat=<minLat>/minLong=<minLong>/maxLat=<maxLat>/maxLong=<maxLong>', methods=['GET'])
def retrieveToilet(minLat, minLong, maxLat, maxLong):
    return to_json(toilet.getToilet(minLat, minLong, maxLat, maxLong))

@App.route('/toilets/rating=<rating>', methods=['GET'])
def ratingGet(rating):
    return to_json(toilet.searchByRating(rating))