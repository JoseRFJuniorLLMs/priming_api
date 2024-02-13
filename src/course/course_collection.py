from typing import List

from src.status.status import Status


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

    def mongo(self):
        pass