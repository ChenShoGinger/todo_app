from pymongo import MongoClient
from typing import Dict

#DB connection data

client = MongoClient("mongodb://db:27017")
db = client["todo-db"]
collection = db["todos"]

def create_todo(todo_data):
    collection.insert_one(todo_data)
    return todo_data

def get_todos():
    return list(collection.find({}, {'_id': False}))

def update_todo(category: str, task_id: int, todo_data: Dict):
    result = collection.update_one({"category": category, "id": task_id}, {"$set": todo_data})
    print(todo_data)
    return result.matched_count > 0

def delete_todo(category: str, task_id: int):
    result = collection.delete_one({"category": category, "id": task_id})
    return result.deleted_count > 0

