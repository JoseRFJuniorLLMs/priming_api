import re

from bson import ObjectId

from fastapi import APIRouter

from repository.mongodb import MongoDB as db
from src.course.course_collection import CourseCollection

from fastapi import HTTPException

course_router = APIRouter(
    prefix="/api/v1/courses",
)

class CourseService:
    @staticmethod
    @course_router.post("/")
    def create_course(course_data: CourseCollection):
        return db().save_document(collection="CourseCollection", document=course_data.mongo())

    @staticmethod
    @course_router.put("/")
    def update_course(course_data: CourseCollection):
        db().update_document(
            collection="CourseCollection",
            key={"_id": course_data.id},
            document=course_data.mongo(),
        )

    @staticmethod
    @course_router.delete("/{course_id}")
    def delete_course(course_id: str):
        db().delete_by_key(collection="CourseCollection", key={"_id": ObjectId(course_id)})

    @staticmethod
    @course_router.get("/")
    def list_courses():
        try:
            courses = db().get_by_filter(collection="CourseCollection", key={})
            return courses
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    @staticmethod
    @course_router.get("/{course_id}")
    def get_course_by_id(course_id: str):
        return db().get_by_key(collection="CourseCollection", key={"_id": ObjectId(course_id)})

    @staticmethod
    @course_router.get("/name/{course_name}")
    def get_course_by_name(course_name: str):
        regex = re.compile(f".*{course_name}.*", re.IGNORECASE)
        return db().get_by_filter(collection="CourseCollection", key={"name": regex})
