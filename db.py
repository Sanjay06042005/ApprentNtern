from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # load from .env file

uri = os.getenv("mongodb+srv://Sanjay:Sanjay@cluster0.ft1o2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db_name = os.getenv("Sanjay")

def get_db():
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    return client[db_name]
