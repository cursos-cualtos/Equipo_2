from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['microservices-course']
collection = db.messages


def message_add(data):
    add_message(data)

def get_all_messages():
    cursor = collection.find()
    return list(cursor)

def get_message(id):
    result = collection.find_one({'_id': ObjectId(id)})
    return result

def add_message(data):
    id = collection.insert_one(data)
    return id

def edit_message(id, data):
    result = collection.update_one({'_id': ObjectId(id)}, 
        {'$set': data})
    return str(result.modified_count)