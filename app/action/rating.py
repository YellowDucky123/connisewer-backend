from app.database import ratings

def create_rating(user_id, toilet_id, rating):
    return ratings.insert_one({"rating": rating, 
                        "user": user_id, 
                        "toilet": toilet_id}).inserted_id

