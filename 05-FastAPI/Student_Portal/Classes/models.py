from pydantic import BaseModel, Field, EmailStr # type: ignore
from typing import List


class Student(BaseModel):
    student_id: int = Field(..., ge=1000, le=9999, description="Student ID between 1000 - 9999")
    student_name: str = Field(..., description="Student Name")
    student_email: EmailStr = Field(..., description="Student Email")
    student_age: int = Field(..., ge=18, le=30, description="Student Age")
    student_courses: List[str] = Field(..., description="Student Courses")
    address: str = Field(None, title="Address", max_length=50)


class emailUpdate(BaseModel):
    email : EmailStr

