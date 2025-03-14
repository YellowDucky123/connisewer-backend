from bson import json_util, ObjectId
import json

def to_json(thing):
    return json.loads(json_util.dumps(thing))

def id_query(id):
    return { "_id": ObjectId(id) }


