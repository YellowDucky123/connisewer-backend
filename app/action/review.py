from app.database import reviews
from flask import jsonify
from datetime import datetime

def create_review(user_id, toilet_id, text, rating):
    date = datetime.now().strftime("%Y-%m-%d")
    return reviews.insert_one({"text": text, 
                        "rating": rating,
                        "user": user_id, 
                        "toilet": toilet_id,
                        "date": date}).inserted_id

def delete_review(review_id):
    reviews.delete_one({"_id": review_id})
    return jsonify(message="review deleted"), 200


