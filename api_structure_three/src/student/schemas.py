from pydantic import BaseModel
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