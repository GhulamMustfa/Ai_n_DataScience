# poetry run uvicorn 06-DataBase.sql:app

from fastapi import FastAPI  # type: ignore
from pymongo import MongoClient  # type: ignore
from dotenv import load_dotenv # type: ignore
import os

app = FastAPI()

load_dotenv()
client = MongoClient(os.getenv("DB_URI"))

print(os.getenv("DB_URI"))

db = client["Learning"]
collection = db["FastAPI"]


@app.get("/")
def read_root():
    return {"Status": "Server is running"}


