from app.database import reviews
from flask import jsonify, session
from datetime import datetime

def create_review(user_id, toilet_id, text, rating):
    date = datetime.now().strftime("%Y-%m-%d")
    return reviews.insert_one({"text": text, 
                        "rating": rating,
                        "user": user_id, 
                        "toilet": toilet_id,
                        "date": date}).inserted_id

def delete_review(review_id):
    return reviews.delete_one({"_id": review_id})

def searchByToiletId(toiletId):
    avg = None
    r = reviews.find({"toilet": int(toiletId)})
    reviews_processed = list(
        reviews.aggregate([
        {
            "$match": {
                "toilet": int(toiletId)
            } 
        },
        {
            "$group": {
                "_id": None,
                "avg": { "$avg": "$rating" }
            }
        }
        ])
    )
    if reviews_processed:
        avg = reviews_processed[0]['avg']
    return {"reviews": r, "average": avg}

