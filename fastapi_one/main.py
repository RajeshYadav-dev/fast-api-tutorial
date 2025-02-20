from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
#http://127.0.0.1:8000
async def get_message()->dict:
  return {"message":"Hello World"}

@app.get("/message")
#http://127.0.0.1:8000/hello
async def get_gello()->dict:
  return  {"message":"hello World"}

@app.get("/name/{name}")
#http://127.0.0.1:8000/name/Rajesh
async def get_name(name:str)->dict:
  return {"message":f"Hello {name}"}

@app.get("/city/{city}")
#http://localhost:8000/city/Delhi?name=Rajesh
async def get_name_age(city:str,name:str)->dict:
  return {"city":f"{city}","name":name}

'''
http://localhost:8000/data/
{
  
  "user": "User",
  "age": 0
}

http://localhost:8000/data?name=Rajesh
{
  "user": "Rajesh",
  "age": 0
}

http://localhost:8000/data?name=Rajesh&age=26
{
  "user": "Rajesh",
  "age": 26
}
'''

@app.get("/data")

async def get_optional_default(name:Optional[str]="User",age:int=0)->dict:
  return {"user":f"{name}","age":age}



'''
http://localhost:8000/create-book
{
  "name":"Rajesh Yadav",
  "author":"Rakesh Mishra",
  "price":"34"
}
'''
class CreateBook(BaseModel):
  name :str
  author :str
  price :int
  
@app.post("/create-book")  
async def create_book(bookModel:CreateBook):
  return {
    "name":bookModel.name,
    "author":bookModel.author,
    "price":bookModel.price
  }
  