
from bson import ObjectId

from typing import List

from src.model.status import Status


class StudentCollection:
    def __init__(self):
        self.id: str
        self.name: str
        self.email: str
        self.tax_identification_number: str
        self.personal_identification_number: str
        self.login: str
        self.password: str
        self.status: Status = Status.ACTIVE
        self.course: List[str]
        self.prime: List[str]