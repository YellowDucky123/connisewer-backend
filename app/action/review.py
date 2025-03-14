from app.database import database
from datetime import datetime

reviews = database["reviews"]

def create_review(user_id, toilet_id, text):
    return reviews.insert_one({"text": text, 
                        "user": user_id, 
                        "toilet": toilet_id,
                        "date": datetime.now().strftime("%Y-%m-%d")})


