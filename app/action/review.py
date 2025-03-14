from app.database import reviews
from datetime import datetime

def create_review(user_id, toilet_id, text):
    return reviews.insert_one({"text": text, 
                        "user": user_id, 
                        "toilet": toilet_id,
                        "date": datetime.now().strftime("%Y-%m-%d")})


