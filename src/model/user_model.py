from datetime import datetime
from enum import Enum
from typing import Optional, List

from bson import ObjectId

from model.mongodb_model import OID, MongoModel

class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"

class Status(Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class User(MongoModel):
    id: OID = str(ObjectId())
    name: str
    gender: Gender
    email: str
    tax_identification_number: str
    personal_identification_number: str
    login: str
    password: str
    status: Status = Status.ACTIVE
    course: List[str]
    lesson: List[str]
    prime: List[str]
