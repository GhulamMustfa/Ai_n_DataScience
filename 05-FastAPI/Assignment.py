# https://github.com/techloset/agentic-ai/blob/master/assingments/assignment1.md

# poetry run uvicorn 05-FastAPI.Assignment:app

from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
from typing import Optional
import re


app = FastAPI()


class Student(BaseModel):
    name: str
    email: str
    age: int
    address: list[str]

@app.post("/students/register")
def register_student(student: Student):
    return {"student": student}
    


@app.post("/students/{student_id}/email")
def update_email(student_id: int, email: str):
    return {"student_id": student_id,
            "email": email}



@app.get("/")
def get_student_info():
    return {"Get": "Student Information"}


@app.get("/students/{student_id}")
def get_studentID(student_id: int, include_grades: bool, semester: str = r"^(Fall|Spring|Summer)\d{4}$"):
    if student_id < 1000 or student_id > 9999:
        return {"Error": "ID should be between 1000 and 9999"}
        # raise ValueError("ID should be between 1000 and 9999")
    return {"student_id": student_id,
            "include_grades": include_grades,
            "semester": semester}

