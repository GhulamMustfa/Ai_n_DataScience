# poetry run uvicorn 06-DataBase.sql:app

from fastapi import FastAPI  # type: ignore
from pymongo import MongoClient  # type: ignore
from dotenv import load_dotenv # type: ignore
import os
from pydantic import BaseModel # type: ignore
import datetime
# from bson.objectid import ObjectId # type: ignore

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
        print(f"Error connecting to DataBase{e}")
        return None


client = check_db_client()
db = client["Learning"]
collection = db["FastAPI"]

class ToDo(BaseModel):
    title: str
    description: str
    status: str


@app.get("/")
def check_server():
    return {"Status": "Server is running"}


@app.get("/todos")
def read_todos():
    try:
        todos = db.todos.find()
        # listtodos = []
        # for todo in todos():
        #     listtodos.append({
        #         "id": str(todo["_id"]),
        #         "title": todo["title"],
        #         "description": todo["description"],
        #         # "status": todo["status"],
        #         "created_at": todo["created at"],
        #         "completed": todo["completed"]
        #     })
        return db.todos
        # return {
        #     "data": listtodos,
        #     "error": None,
        #     "message": "Todos read successfully",
        #     "status": "success"
        #     }
    except Exception as e:
        print(f"Error reading todos: {e}")
        return {
            "data": [],
            "error": "Error reading todos",
            "message": str(e),
            "status": "failed"
            }
