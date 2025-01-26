# https://github.com/techloset/agentic-ai/blob/master/assingments/assignment1.md

# poetry run uvicorn 05-FastAPI.Assignment:app

from fastapi import FastAPI, Path, Query # type: ignore
from pydantic import BaseModel, EmailStr # type: ignore


app = FastAPI()

@app.get("/")
def get_student_info():
    return {"Get": "Student Information"}

@app.get("/students/{student_id}")
def get_student_id(student_id: int = Path(ge=1000, le=9999),
                  include_grades: bool = Query,
                  semester: str = Query(None, regex="^(Fall|Spring|Summer)\d{4}$")):
    return {"student_id": student_id,
            "include_grades": include_grades,
            "semester": semester}


class Student(BaseModel):
    name: str
    email: EmailStr
    age: int = Path(ge=18, le=30)
    course: list[str]

@app.post("/students/register")
def register_student(student: Student):
    return{student: student}

@app.put("/students/{student_id}/email")
def update_email(email: str, student_id: int = Path(ge=1000, le=9999)):
    return {"student_id": student_id,
            "email": email}




# , name: str, email: EmailStr, age: int, course: list[str]
