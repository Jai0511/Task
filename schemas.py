from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Base classes for Course and Student
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class StudentBase(BaseModel):
    name: str
    email: EmailStr

# Create classes (used in POST requests)
class CourseCreate(CourseBase):
    pass

class StudentCreate(StudentBase):
    pass

# Output-only schemas (used for GET responses)
class CourseOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True  # Allows conversion of SQLAlchemy models to Pydantic models

class StudentOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    courses: List[CourseOut] = []

    class Config:
        orm_mode = True  # Allows conversion of SQLAlchemy models to Pydantic models

class CourseOutFull(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    students: List[StudentOut] = []

    class Config:
        orm_mode = True  # Allows conversion of SQLAlchemy models to Pydantic models

# Enrollment request schema (used in POST requests)
class EnrollmentRequest(BaseModel):
    student_id: int
    course_id: int
