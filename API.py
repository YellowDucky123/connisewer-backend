# APIs here
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# importing os module for environment variables
import os
# importing necessary functions from dotenv library
from dotenv import load_dotenv, dotenv_values 
# loading variables from .env file
load_dotenv() 
# # accessing and printing value
# print(os.getenv(&quot;MY_KEY&quot;))

# connect to database
uri = "mongodb+srv://connisewer:" + os.getenv("password") + "@connisewer.wljsc.mongodb.net/?retryWrites=true&w=majority&appName=connisewer"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")

    database = client["test_database"]
    database.create_collection("example_collection")

    collection_list = database.list_collections()
    for c in collection_list:
        print(c)
except Exception as e:
    print(e)


