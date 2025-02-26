from fastapi import APIRouter, Depends, HTTPException, Path, Query, Body# type: ignore
from Classes.models import Student, emailUpdate


authRouter = APIRouter()


@authRouter.get("/students/{student_id}")
def get_student_id(student_id: int = Path(ge=1000, le=9999, description="Student ID between 1000 - 9999"),
                  include_grades: bool = Query(description="Include grades True or False"),
                  semester: str = Query(None, regex="^(Fall|Spring|Summer)\d{4}$")):
      return {"Student_id": student_id,
            "Grades": include_grades,
            "Semester": semester}


@authRouter.post("/students/register")
def register_student(student: Student):
    try:
        return{"Status": "Success",
            "Data": student}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@authRouter.put("/students/update/{student_id}/email")
def update_email(student_id: int = Path(ge=1000, le=9999, description="Student ID between 1000 - 9999"),
                 email: emailUpdate = Body(...)):
    return {"Student_id": student_id,
            "Email": email.email}


@authRouter.delete("/students/delete/{student_id}")
def delete_student(student_id: int = Path(ge=1000, le=9999, description="Student ID between 1000 - 9999")):
    return {"Student_id": student_id,
            "Status": "Deleted"}

