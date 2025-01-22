# from fastapi import FastAPI # type: ignore

# app = FastAPI()

# @app.get("/")
# def get_hello_world():
#     return {"Hello": "World"}

# # @app.get("/login")
# # def get_login():
# #     return {"Hello": "World"
# #             "Login" "Success"}

# # @app.get("/signup")
# # def get_signup():
# #     return {"Hello": "World"}

# @app.get("/search")
# def search_items(q: str, limit: int = 10):
#     return {"query": q, "limit": limit}

# # poetry run uvicorn 05-FastAPI.main:app
# # http://localhost:8000/login


from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int
    email: Optional[str] = None
    address: Optional[str] = None
    

@app.post("/user/{id}")
def create_user(person: Person,id:int,query: Optional[str] = None):
    try:
      if id < 100:
        raise ValueError("ID should be greater than 100")
        # delete code?
      return {
                "status": "success",
                "data": {
                    "query": query,
                    "id": id,
                    "person":person
                    }
      }
    except Exception as e:
      return {
              "message": str(e),
                "status": "error",
                "data": None
      }

@app.get("/user")
def read_root(id: str,name:str,age:int):
    try:
        # Your code goes here
        return {
            "status": "success",
            "data": {
                "id": id,
                "profile_url":"url.com",
                "email": "abc@gmail.com",
                "name": name,
                "age": age,
                "address":["123 Main Street", "Apt 4", "New York, NY 10001"],
            }
        }
      
    except Exception as e:
      return {
           "message": str(e),
           "status": "error",
           "data": None
          }


