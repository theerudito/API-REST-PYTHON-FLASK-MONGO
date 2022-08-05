import os
from dotenv import dotenv_values
config = dotenv_values(".env")  # Load .env file
from pymongo import MongoClient
import certifi


MONGO_URI = "YOUR MONGO URI"

cetificate = certifi.where()

def DB_CONNECTION():
    try:
        client = MongoClient( MONGO_URI, tlsCAFile=cetificate)
         # CREATE DATABASE
        print("Connected to MongoDB")
        return client['PYTHON_DB']
    except Exception as e:
        print("Error connect to MongoDB: ", e)
        return None

   
    