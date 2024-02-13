from fastapi import APIRouter

from logger import log
from student.student_collection import student_collection
from services import student_service as service

crud_router = APIRouter(
    prefix="/api/student",
)

@crud_router.get("/")
def index():
    log().info("Welcome!!")
    return {"Welcome!!": "Student REST"}