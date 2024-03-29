import re
from typing import List

from bson import ObjectId

from model.user_model import User
from repository.mongodb import MongoDB as db

COLLECTION_USER = "StudentCollection"


def create_user(user_data: User):
    return db().save_document(collection=COLLECTION_USER, document=user_data.dict())


def update_user(user_data: User):
    db().update_document(
        collection=COLLECTION_USER,
        key={"_id": user_data.id},
        document=user_data.dict(),
    )


def delete_by_id(user_id: str):
    db().delete_by_key(collection=COLLECTION_USER, key={"_id": ObjectId(user_id)})


def get_list_users():
    list_users = db().get_by_filter(collection=COLLECTION_USER, key={})
    return [User(**user) for user in list_users]


def get_user_by_id(user_id: str):
    result = db().get_by_key(collection=COLLECTION_USER, key={"_id": ObjectId(user_id)})
    return User(**result)


def get_user_by_name(user_name: str):
    regex = re.compile(f".*{user_name}.*", re.IGNORECASE)
    list_users = db().get_by_filter(collection=COLLECTION_USER, key={"name": regex})
    return [User(**user) for user in list_users]
