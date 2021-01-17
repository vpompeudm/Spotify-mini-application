from pymongo import MongoClient

client = MongoClient(os.getenv('MONGO_CONN'))
