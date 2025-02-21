from fastapi import status, APIRouter, HTTPException
from typing import List
from .student_data import students
from .schemas import StudentModel, StudentUpdateModel

student_router = APIRouter()

# GET all students
@student_router.get(
    "/",
    response_model=List[StudentModel],
    status_code=status.HTTP_200_OK
)
async def get_all_students():
    return students

# POST create a new student
@student_router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
async def create_student(student_model: StudentModel) -> dict:
    new_student = student_model.model_dump()
    # Optionally, add the new student to your students list or database here
    return new_student

# GET a single student by id
@student_router.get(
    "/{student_id}",
    status_code=status.HTTP_200_OK
)
async def get_a_student(student_id: int) -> dict:
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

# PATCH update a student by id
@student_router.patch(
    "/{student_id}",
    status_code=status.HTTP_200_OK
)
async def update_student(student_id: int, studentModel: StudentUpdateModel) -> dict:
    for student in students:
        if student["id"] == student_id:
            student["name"] = studentModel.name
            student["age"] = studentModel.age
            student["city"] = studentModel.city
            student["standard"] = studentModel.standard
            return student
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

# DELETE a student by id
@student_router.delete(
    "/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
async def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {}  # With 204, no content is expected
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
