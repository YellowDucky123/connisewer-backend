from app.database import toilets, ratings, reviews
from app.utils import id_query
from bson import ObjectId

def get_reviews(id):
    return reviews.find({ "toilet": id})

def getToilet(minLat, minLong, maxLat, maxLong):
    def average(ratings):
        total = 0
        for r in ratings:
            total += ratings.find({"_id": r}).value
        return total / len(ratings)

    print(minLat, minLong, maxLat, maxLong)
    t = toilets.find({
        'location.0': {'$gte': float(minLat), '$lte': float(maxLat)},  # Latitude
        'location.1': {'$gte': float(minLong), '$lte': float(maxLong)} # longitude
    })['rating'] = average(t.ratings)

    return t


def searchByRating(rating):
    return toilets.find({"rating": {"$gte": 1, "$lte": 5}})
# def addToilet()
