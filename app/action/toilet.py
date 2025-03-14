from app.database import toilets
from app.utils import id_query
from bson import ObjectId

def add_review(toilet_id, review_id):
    toilets.update_one(id_query(toilet_id),
                     { "$push": { "reviews": review_id }})


