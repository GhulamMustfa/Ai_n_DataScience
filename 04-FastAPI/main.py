from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def get_hello_world():
    return {"Hello": "World"}

@app.get("/login")
def get_login():
    return {"Hello": "World"
            "Login" "Success"}

@app.get("/signup")
def get_signup():
    return {"Hello": "World"}

# poetry run uvicorn 04-FastAPI.main:app
# http://localhost:8000/login
