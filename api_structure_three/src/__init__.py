from fastapi import FastAPI
from src.student.routes import student_router 

version = "v1"
app = FastAPI(
    title="Student API",
    description="REST API for Student review web services",
    version=version
)

app.include_router(student_router, prefix=f"/api/{version}/students", tags=["student"])
