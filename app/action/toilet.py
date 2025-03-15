from app.database import toilets, ratings, reviews
from app.utils import id_query
from bson import ObjectId

def add_review(toilet_id, review_id):
    toilets.update_one(id_query(toilet_id),
                     { "$push": { "reviews": review_id }})

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
