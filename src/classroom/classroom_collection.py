import re
from typing import List

from bson import ObjectId

from repository.mongodb import MongoDB as db

from typing import List


class ClassroomCollection:
    def __init__(self):
        self.id: str
        self.alunoId: str
        self.curso: str
        self.modulo: str
        self.prime: List[str]
        self.target: List[str]
        self.phrases: List[str]
