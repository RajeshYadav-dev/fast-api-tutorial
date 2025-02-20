from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List
from fastapi.exceptions import HTTPException


app = FastAPI()

students = [
  {
    "id":1,
    "name":"Rajesh Yadav",
    "age":20,
    "city":"Delhi",
    "standard":5
  },
  {
    "id":2,
    "name":"Rakesh Yadav",
    "age":21,
    "city":"patna",
    "standard":6
  },
  {
    "id":3,
    "name":"Ramesh Yadav",
    "age":23,
    "city":"Guntur",
    "standard":8
  },
  {
    "id":4,
    "name":"Kanchan Yadav",
    "age":22,
    "city":"Bihar",
    "standard":12
  },
]

class StudentModel(BaseModel):
  id: int
  name: str
  age: int
  city: str
  standard: int
  
class StudentUpdateModel(BaseModel):
  name: str
  age: int
  city: str
  standard: int  

@app.get("/students",response_model=List[StudentModel],status_code=status.HTTP_200_OK)
async def get_all_students():
  return students

@app.post("/students",status_code=status.HTTP_201_CREATED)
async def get_all_students(student_model:StudentModel)->dict:
  new_student = student_model.model_dump()
  return new_student

@app.get("/student/{student_id}",status_code=status.HTTP_200_OK)
async def get_a_student(student_id:int)->dict:
  for student in students:
    if student["id"] == student_id:
      return student
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student not found")

@app.patch("/student/{student_id}",status_code=status.HTTP_200_OK)
async def get_a_student(student_id:int,studentModel:StudentUpdateModel)->dict:
  for student in students:
    if student["id"] == student_id:
      student["name"] = studentModel.name
      student["age"] = studentModel.age
      student["city"] = studentModel.city
      student["standard"] = studentModel.standard
      return student
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student not found")  

@app.delete("/student/{student_id}",status_code=status.HTTP_204_NO_CONTENT)
async def get_a_student(student_id:int):
  for student in students:
    if student["id"] == student_id:
      students.remove(student)
      return {}
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Student not found")  