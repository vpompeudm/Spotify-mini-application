from flask import Flask, jsonify
from markupsafe import escape
from flask import request
from dotenv import load_dotenv
from db import get_all_artists, insert_artist
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
         





    