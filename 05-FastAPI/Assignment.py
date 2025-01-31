# https://github.com/techloset/agentic-ai/blob/master/assingments/assignment1.md

# poetry run uvicorn 05-FastAPI.Assignment:app

from fastapi import FastAPI, HTTPException , Path, Query # type: ignore
from pydantic import BaseModel, EmailStr # type: ignore


app = FastAPI()

# Data
students = {
    1000: {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "age": 22,
        "courses": ["Mathematics", "Physics", "Chemistry"]
    }
}

# Class defining student
class Student(BaseModel):
    name: str
    email: EmailStr
    age: int = Path(ge=18, le=30)
    course: list[str]

# Class to update email
class emailUpdate(BaseModel):
    email : EmailStr


# Base Route
@app.get("/")
def get_student_info():
    return {"Getting": "Student Information"}

# Route to get student information
# path parameter to get student id
# query parameters to include grades and optional semester
@app.get("/students/{student_id}")
def get_student_id(student_id: int = Path(ge=1000, le=9999, description="Student ID between 1000 - 9999"),
                  include_grades: bool = Query(description="Include grades True or False"),
                  semester: str = Query(None, regex="^(Fall|Spring|Summer)\d{4}$")):
    
    # # validating student_id
    # if student_id < 1000 or student_id > 9999:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="Student_id must be between 1000 - 9999"
    #     )

    # # validating include_grades    
    # if include_grades not in [True, False]:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="include_grades must be boolean"
    #     )

    # # validating semester    
    # if semester not in ["Fall", "Spring", "Summer"]:
    #     raise HTTPException(
    #         status_code=404,
    #         detail="Semester must be Fall, Spring or Summer"
    #     )

    # after validation return the values
    return {"Student_id": student_id,
            "Grades": include_grades,
            "Semester": semester}



@app.post("/students/register")
def register_student(student: Student):
    return{"Status": "Success",
       "Data": student}


@app.put("/students/{student_id}/email")
def update_email(email: emailUpdate, student_id: int = Path(ge=1000, le=9999)):
    return {"student_id": student_id,
            "email": email}




# , name: str, email: EmailStr, age: int, course: list[str]
# poetry run uvicorn 05-FastAPI.Assignment:app
