from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db = []


class Course(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None


@app.get("/")
def read_root():
    return {"Welcome": "Welcome to the fastAPI"}


@app.get("/courses")
def read_courses():
    return db


@app.get("/courses/{course_id}")
def read_course(course_id: int):
    return db[course_id - 1]


@app.post("/courses")
def create_course(course: Course):
    db.append(course.dict())
    return db[-1]


@app.put("/courses/{course_id}")
def update_course(course_id: int, course: Course):
    db[course_id-1] = course.dict()
    return {
        "success": True,
        "message": "Course updated successfully",
        "data": db[course_id - 1]
    }


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    db.pop(course_id - 1)
    return {
        "message": "Course with id {} deleted".format(course_id)
    }
