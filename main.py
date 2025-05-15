from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models, schemas

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/", response_model=schemas.StudentOut)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    db_student = models.Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@app.post("/courses/", response_model=schemas.CourseOut)
def create_course(course: schemas.CourseCreate, db: Session = Depends(get_db)):
    db_course = models.Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@app.post("/enroll/")
def enroll_student(enrollment: schemas.EnrollmentRequest, db: Session = Depends(get_db)):
    student = db.query(models.Student).get(enrollment.student_id)
    course = db.query(models.Course).get(enrollment.course_id)
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": "Student enrolled successfully"}

@app.get("/students/{id}", response_model=schemas.StudentOut)
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).get(id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return studentŚ

@app.get("/courses/{id}", response_model=schemas.CourseOutFull)
def get_course(id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).get(id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course