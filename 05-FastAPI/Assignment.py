# https://github.com/techloset/agentic-ai/blob/master/assingments/assignment1.md

# poetry run uvicorn 05-FastAPI.Assignment:app

from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def get_hello_world():
    return {"Get": "Student Information"}

@app.get("/students/{student_id}")
def get_studentID(student_id: int):
    if student_id < 1000 or student_id > 9999:
        return("ID should be between 1000 and 9999")
        # raise ValueError("ID should be between 1000 and 9999")
    return {"student_id": student_id}

@app.get("/grades")
def grades_semester(q: bool, semester: str):
    return {"query": q, 
            "semester": semester}

