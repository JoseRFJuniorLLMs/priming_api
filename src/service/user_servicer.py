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
    users = []
    for user in list_users:
        user_id = ObjectId(user['_id'])
        user_data = {
            '_id': user_id,
            'name': user.get('name', ''),
            'gender': user.get('gender', 'Male'),
            'email': user.get('email', ''),
            'tax_identification_number': user.get('tax_identification_number', ''),
            'personal_identification_number': user.get('personal_identification_number', ''),
            'login': user.get('login', ''),
            'password': user.get('password', ''),
            'status': user.get('status', 'Active').title(),  # Ensure the default value is properly formatted
            'course': user.get('course', ''),
            'lesson': user.get('lesson', []),
            'prime': user.get('prime', '')
        }
        users.append(User(**user_data))
    return users





def get_user_by_id(user_id: str):
    result = db().get_by_key(collection=COLLECTION_USER, key={"_id": ObjectId(user_id)})
    return User(**result, id=ObjectId(result['_id']))


def get_user_by_name(user_name: str):
    regex = re.compile(f".*{user_name}.*", re.IGNORECASE)
    list_users = db().get_by_filter(collection=COLLECTION_USER, key={"name": regex})
    return [User(**user, id=ObjectId(user['_id'])) for user in list_users]
