from app.database import toilets
from app.utils import id_query
from bson import ObjectId

def add_review(toilet_id, review_id):
    toilets.update_one(id_query(toilet_id),
                     { "$push": { "reviews": review_id }})

def getToilet(minLat, minLong, maxLat, maxLong):
    print(minLat, minLong, maxLat, maxLong)
    return toilets.find({
        'location.0': {'$gte': float(minLat), '$lte': float(maxLat)},  # Latitude
        'location.1': {'$gte': float(minLong), '$lte': float(maxLong)} # longitude
})

def searchByRating(rating):
    return toilets.find({"rating": {"$gte": 1, "$lte": 5}})
# def addToilet()