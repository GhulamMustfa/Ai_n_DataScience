from fastapi import FastAPI 
from pymongo import MongoClient 
from dotenv import load_dotenv
import os


load_dotenv()
app = FastAPI()
print(os.getenv("DB_URI"))
client = MongoClient(os.getenv("DB_URI"))


@app.get("/")
def read_root():
    return {"Status": "Server is running"}

