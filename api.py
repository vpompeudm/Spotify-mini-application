from flask import Flask
from markupsafe import escape
from flask import request
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv('MONGO_CONN'))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

    