from flask import Flask, jsonify
from markupsafe import escape
from flask import request
from dotenv import load_dotenv
from db import get_all_artists, insert_artist
from sp import search_artist, top_tracks
import os 
import json
from bson import json_util

load_dotenv()

print(os.getenv('MONGO_CONN'))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/artists', methods = ['GET', 'POST'])
def artists_handler():
    if request.method == 'POST':
        insert_artist(request.json['artist_name'])
        return "ok"
    elif request.method == 'GET':
        artist_list = get_all_artists()
        response = {'artists':json.dumps(artist_list,default=json_util.default)}
        return response
         
@app.route('/toptracks', methods = ['GET'])
def tracks_from_db():
    artist_list = get_all_artists()
    response = []
    for artist in artist_list:
        formatted_track = get_top3_tracks(artist)
        response.append(formatted_track)
    response = {'artists':json.dumps(response,default=json_util.default)}
    return response


def get_top3_tracks(artist):
    artist_spotify = search_artist(artist['name'])
    artist_id = artist_spotify['id']
    tracks = top_tracks(artist_id)
    formatted_tracks = []
    for track in tracks[:3]:
        formatted_track = {'name':track['name'], 'URL':track['external_urls']['spotify']}
        formatted_tracks.append(formatted_track)
    artist_tracks = {'artist':artist_spotify['name'], 'top_tracks':formatted_tracks}
    return artist_tracks









    