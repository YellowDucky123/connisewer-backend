from flask import jsonify, request
from flask_cors import CORS
from .database import client, database
from .utils import to_json
from . import App  # Ensure this is after Flask is created

# Move other imports after app
from .action import user
from .action import toilet
from .action import auth
from .action import review

CORS(App, origins=["http://localhost:3000", "https://connisewer.vercel.app"])

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

#---------------------------------------------------------------------------------------#
#------------------------------------ USER ROUTES --------------------------------------#
#---------------------------------------------------------------------------------------#

# add a user
@App.route('/user/register', methods=['POST'])
def registerUser():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid request"}), 400

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    token = user.register(username, email, password)
    return jsonify({"token": token}), 201

@App.route('/user/edit', methods=['PUT'])
def updateReview():
    id = request.args['review_id']
    text = request.args['text']
    rating = request.args['rating']
    return user.change_review(id, text, rating)

@App.route('/user/id=<id>', methods=['GET'])
def getById(id):
    return to_json(user.find_by_id(id))


@App.route('/user/id=<id>/reviews', methods=['GET'])
def get_reviews(id):
    return to_json(user.get_reviews(id))
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


@App.route('/reviews/toiletId=<id>', methods=['GET'])
def getToiletwithId(id):
    return to_json(review.searchByToiletId(id))

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

# #---------------------------------------------------------------------------------------#
# #------------------------------------ AUTH ROUTES --------------------------------------#
# #---------------------------------------------------------------------------------------#

@App.route('/login', methods=['POST'])
def login():
    username = request.args['username']
    email = request.args['email']
    password = request.args['password']
    return auth.authentication(username, email, password)

@App.route('/login', methods=['DELETE'])
def logout():
    access_token = request.args['access_token']
    return auth.userLogout(access_token)
