import re
from typing import List

from bson import ObjectId

from repository.mongodb import MongoDB as db
class LessonCollection:
    def __init__(self):
        self._id: str
        self.name: str
        self.youtubeUrl: str
        self.course: str
        self.time: str