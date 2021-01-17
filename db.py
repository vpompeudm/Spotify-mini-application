from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('MONGO_CONN'))

def insert_artist(artist_name):
    db = client['Spotify']
    artists_collection = db['Artists']

    post = {'name':artist_name}
    artists_collection.insert(post)
