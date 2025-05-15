# Student API with FastAPI

A simple student-course enrollment API using FastAPI, SQLAlchemy, and SQLite.

## Features

- Add students and courses
- Enroll students in courses
- View student/course details
- Delete students, courses, and enrollments

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic

## Setup Instructions

1. Create a virtual environment:
   python -m venv venv

2. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```

- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

3. Install dependencies:
   pip install -r requirements.txt

4. Run the application:
   uvicorn main:app --reload

5. Access the Swagger UI:
   https://127.0.0.1:8000/docs
