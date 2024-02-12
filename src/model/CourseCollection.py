import re
from typing import List

from bson import ObjectId

from repository.mongodb import MongoDB as db

from typing import List

from src.model.Status import Status


class CourseCollection:
    def __init__(self):
        self._id: str
        self.name: str
        self.objective: str
        self.content: List[str]
        self.lessons: List[str]
        self.category: str
        self.level: str
        self.price: str
        self.status: Status = Status.ACTIVE