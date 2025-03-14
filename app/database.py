# APIs here
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file

def connect():
    load_dotenv() 
    password = os.getenv('password')
    if password == None:
        raise Exception("No password in the environment")
    uri = "mongodb+srv://connisewer:" + password  + "@connisewer.wljsc.mongodb.net/?retryWrites=true&w=majority&appName=connisewer"
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client

try:
    client = connect()
    client.admin.command('ping')

    print("Connected to the database")

    database = client["connisewer"] 
    
    for name in ['toilets', 'users', 'reviews', 'ratings']:
        if not hasattr(database, name):
            database.create_collection(name)

    toilets = database["toilets"]
    users = database["users"]
    reviews = database["reviews"]
    ratings = database["ratings"]

except Exception as e:
    print(e)


