import re
from typing import List

from bson import ObjectId

from repository.mongodb import MongoDB as db
class ModuleCollection:
    def __init__(self):
        self.id: str
        self.prime: str
        self.target: str
        self.text: str