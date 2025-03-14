from flask import Flask
from API import client

app = Flask(__name__)

database = client["test_database"]
collection_list = database.list_collections()

result = ""

for c in collection_list:
    result += "<p>" + c.get("name") + "</p>"

@app.route('/')
def hello():
    return result

