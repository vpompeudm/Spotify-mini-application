from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv('MONGO_CONN'))

db = client['Spotify']
artists_collection = db['Artists']

def insert_artist(artist_name):
    post = {'name':artist_name}
    artists_collection.insert(post)

def get_all_artists():
    return artists_collection.find( {} )
