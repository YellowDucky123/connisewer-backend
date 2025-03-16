from flask import jsonify, request, session
from flask_cors import CORS
from flask_session import Session
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

    return user.register(username, email, password)

# returns everything, including the reviews
@App.route('/user/info/id=<id>', methods=['GET'])
def user_info(id):
    return to_json(user.get_info(id))

# update a review from a user
@App.route('/user/edit', methods=['PUT'])
def updateReview():
    sess = session.get('user_info')
    if not sess:
        return jsonify(message='you are not logged in'), 401
    
    id = sess[0]
    text = request.args['text']
    rating = request.args['rating']
    
    return user.change_review(id, text, rating)

# search for a user based on their user id, does not have reviews (refer to user_info())
@App.route('/user/id=<id>', methods=['GET'])
def getById(id):
    sess = session.get('user_info')
    if not sess:
        return jsonify(message='you are not logged in'), 401
    
    return to_json(user.find_by_id(id))

# get reviews by a certain user
@App.route('/user/id=<id>/reviews', methods=['GET'])
def get_user_reviews(id):
    sess = session.get('user_info')
    if not sess:
        return jsonify(message='you are not logged in'), 401
    
    return to_json(user.get_reviews(id))

@App.route('/toilet/id=<id>/reviews', methods=['GET'])
def get_toilet_reviews(id):
    sess = session.get('user_info')
    if not sess:
        return jsonify(message='you are not logged in'), 401
    
    return to_json(toilet.get_reviews(id))

# delete a user
@App.route('/user/delete', methods=['DELETE'])
def deleteUser():
    res = session.pop("user_info")
    if res is None:
        return jsonify(message="error: token does not exist"), 400
    
    user.delete(res[0])
    return jsonify(message="user deleted"), 200

    



# #---------------------------------------------------------------------------------------#
# #------------------------------------ REVIEW ROUTES ------------------------------------#
# #---------------------------------------------------------------------------------------#

# user makes a review
@App.route('/user/post-review', methods=['POST'])
def makeReview():
    sess = session.get('user_info')
    if not sess:
        return jsonify(message='you are not logged in'), 401
    
    user_id = sess[0]
    toilet_id = request.args["toilet_id"]
    text = request.args["text"]
    rating = int(request.args["rating"])

    user.post_review(user_id, toilet_id, text, rating)
    return "success"

# get all reviews that has the toilet id and avg rating
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




# search for toilets on position
@App.route('/toilets/minLat=<minLat>/minLong=<minLong>/maxLat=<maxLat>/maxLong=<maxLong>', methods=['GET'])
def retrieveToilet(minLat, minLong, maxLat, maxLong):
    sess = session.get('user_info')
    if not sess:
        return jsonify(message='you are not logged in'), 401
    
    return to_json(toilet.getToilet(minLat, minLong, maxLat, maxLong))

# get a toilet based on rating
@App.route('/toilets/rating=<rating>', methods=['GET'])
def ratingGet(rating):
    sess = session.get('user_info')
    if not sess:
        return jsonify(message='you are not logged in'), 401
    
    return to_json(toilet.searchByRating(rating))

# #---------------------------------------------------------------------------------------#
# #------------------------------------ AUTH ROUTES --------------------------------------#
# #---------------------------------------------------------------------------------------#

# user login
@App.route('/auth/login', methods=['POST'])
def login():
    try:
        data = request.json
        
        if not data:
            return jsonify({"error": "Invalid request"}), 400
        
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        return auth.authentication(email, password)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# user logout
@App.route('/auth/logout', methods=['DELETE'])
def logout():
    return auth.userLogout()
