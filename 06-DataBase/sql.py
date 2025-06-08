# poetry run uvicorn 06-DataBase.sql:app

from fastapi import FastAPI  # type: ignore
from pymongo import MongoClient  # type: ignore
from dotenv import load_dotenv # type: ignore
import os
from pydantic import BaseModel # type: ignore
import datetime
from typing import List, Optional, Dict, Any
from bson import ObjectId  # type: ignore


app = FastAPI()


load_dotenv()
# client = MongoClient(os.getenv("DB_URI"))
# print(os.getenv("DB_URI"))
def check_db_client():
    try:
        client = MongoClient(os.getenv("DB_URI"))
        print("Connected to DataBase")
        return client
    except Exception as e:
        print(f"Error connecting to DataBase: {e}")
        return None


client = check_db_client()
db = client["Learning"]
collection = db["FastAPI"]

class ToDo(BaseModel):
    title: str
    description: str
    status: str
    created_at: Optional[datetime.datetime] = datetime.datetime.now()


@app.get("/")
def check_server():
    return {"Status": "Server is running"}


@app.get("/todos")
def read_todos():
    try:
        todos = list(collection.find())
        print("Found documents:", todos)  # Debug print
        
        formatted_todos = []
        for todo in todos:
            formatted_todo = {
                "title": todo.get("title", ""),
                "description": todo.get("description", ""),
                "status": todo.get("status", "pending"),
                "created at": todo.get("created at", datetime.datetime.now()),
            }
            formatted_todos.append(formatted_todo)
            
        return {
            "data": formatted_todos,
            "error": None,
            "message": "Todos read successfully",
            "status": "success"
        }
    except Exception as e:
        return {
            "data": [],
            "error": "Error reading todos",
            "message": str(e),
            "status": "failed"
        }


@app.get("/todos/{id}")
def get_todo_by_id(id: str):
    try:
        todo = collection.find_one({"_id": ObjectId(id)})
        if todo is None:
            return {
                "data": [],
                "error": "Todo not found",
                "message": "Todo not found",
                "status": "failed"
            }
        return {
            "data": {
                "id": str(todo["_id"]),
                "title": todo["title"],
                "description": todo["description"],
                "status": todo["status"],
                "created at": todo["created at"],
            },
            "error": None,
            "message": "Todo Read Successfully",
            "status": "Success"
        }
    except Exception as e:
        return {
            "data": [],
            "error": "Error reading todo",
            "message": str(e),
            "status": "failed"
        }






# # Created using AI Model of Cursor AI and its really amazing.
# # Create a new todo
# @app.post("/todos")
# def create_todo(todo: ToDo):
#     try:
#         # Convert Pydantic model to dictionary
#         todo_dict = todo.dict()
        
#         # Insert into MongoDB
#         result = collection.insert_one(todo_dict)
        
#         # Get the inserted document
#         inserted_todo = collection.find_one({"_id": result.inserted_id})
        
#         return {
#             "data": {
#                 "title": inserted_todo.get("title", ""),
#                 "description": inserted_todo.get("description", ""),
#                 "status": inserted_todo.get("status", "pending"),
#                 "created_at": inserted_todo.get("created_at", datetime.datetime.now()),
#                 "completed": inserted_todo.get("completed", False)
#             },
#             "error": None,
#             "message": "Todo created successfully",
#             "status": "success"
#         }
#     except Exception as e:
#         return {
#             "data": None,
#             "error": "Error creating todo",
#             "message": str(e),
#             "status": "failed"
#         }

# # Update a todo
# @app.put("/todos/{todo_id}")
# def update_todo(todo_id: str, todo: ToDo):
#     try:
#         # Convert Pydantic model to dictionary
#         todo_dict = todo.dict()
        
#         # Update in MongoDB
#         result = collection.update_one(
#             {"_id": ObjectId(todo_id)},
#             {"$set": todo_dict}
#         )
        
#         if result.modified_count == 0:
#             return {
#                 "data": None,
#                 "error": "Todo not found",
#                 "message": f"No todo found with id {todo_id}",
#                 "status": "failed"
#             }
        
#         # Get the updated document
#         updated_todo = collection.find_one({"_id": ObjectId(todo_id)})
        
#         return {
#             "data": {
#                 "title": updated_todo.get("title", ""),
#                 "description": updated_todo.get("description", ""),
#                 "status": updated_todo.get("status", "pending"),
#                 "created_at": updated_todo.get("created_at", datetime.datetime.now()),
#                 "completed": updated_todo.get("completed", False)
#             },
#             "error": None,
#             "message": "Todo updated successfully",
#             "status": "success"
#         }
#     except Exception as e:
#         return {
#             "data": None,
#             "error": "Error updating todo",
#             "message": str(e),
#             "status": "failed"
#         }

# # Delete a todo
# @app.delete("/todos/{todo_id}")
# def delete_todo(todo_id: str):
#     try:
#         # Delete from MongoDB
#         result = collection.delete_one({"_id": ObjectId(todo_id)})
        
#         if result.deleted_count == 0:
#             return {
#                 "data": None,
#                 "error": "Todo not found",
#                 "message": f"No todo found with id {todo_id}",
#                 "status": "failed"
#             }
        
#         return {
#             "data": None,
#             "error": None,
#             "message": "Todo deleted successfully",
#             "status": "success"
#         }
#     except Exception as e:
#         return {
#             "data": None,
#             "error": "Error deleting todo",
#             "message": str(e),
#             "status": "failed"
#         }

