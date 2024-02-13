from typing import List

from src.status.status import Status


class StudentCollection:
    def __init__(self):
        id: str
        name: str
        email: str
        tax_identification_number: str
        personal_identification_number: str
        login: str
        password: str
        status: Status = Status.ACTIVE
        course: List[str]
        lesson: List[str]
        prime: List[str]