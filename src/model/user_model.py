from datetime import datetime
from enum import Enum
from typing import Optional, List
from bson import ObjectId
from pydantic import BaseModel, Field

class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

class Status(str, Enum):
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class User(BaseModel):
    id: Optional[ObjectId] = Field(default_factory=ObjectId, alias="_id")
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

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
