import os
from datetime import date, datetime, time
from enum import Enum
from typing import Dict, List

from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from exceptions import mongodb_expection
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class MongoDB:
    def __init__(self):
        self.db = self._get_db()

    def _transform_dict(self, dict_data: dict):
        def validation(v):
            if isinstance(v, date):
                return datetime.combine(v, time())
            if isinstance(v, list):
                return [validation(i) for i in v]
            if isinstance(v, dict):
                return self._transform_dict(v)
            if isinstance(v, Enum):
                return v.value
            return v

        return {k: validation(v) for k, v in dict_data.items()}

    def _get_db(self):
        client = MongoClient(
            "mongodb+srv://junior:debian23@prime.0zjimdw.mongodb.net/primeDB?retryWrites=true&w=majority")
        return client.primeDB

    def save_document(self, collection: str, document: Dict) -> str:
        try:
            result = self.db[collection].insert_one(self._transform_dict(document))
            return str(result.inserted_id)
        except DuplicateKeyError:
            raise mongodb_expection.DuplicateKeyError()

    def update_document(self, collection: str, key: Dict, document: Dict):
        result = self.db[collection].replace_one(key, self._transform_dict(document))
        if result.matched_count == 0:
            raise mongodb_expection.DocumentNotFoundError(key)

    def get_by_filter(self, collection: str, key: Dict) -> List[Dict]:
        result = self.db[collection].find(key)
        if result:
            return result
        raise mongodb_expection.DocumentNotFoundError(key)

    def get_by_key(self, collection: str, key: Dict) -> Dict:
        result = self.db[collection].find_one(key)
        if result:
            return result
        raise mongodb_expection.DocumentNotFoundError(key)

    def delete_by_key(self, collection: str, key: Dict):
        result = self.db[collection].delete_one(key)
        if result:
            return result
        raise mongodb_expection.DocumentNotFoundError(key)

    def test_connection(self):
        try:
            # Conectar ao MongoDB
            client = MongoClient("mongodb+srv://junior:debian23@prime.0zjimdw.mongodb.net/?retryWrites=true&w=majority")
            client.get_database("primeDB")
            print("Conexão bem-sucedida ao MongoDB!")
            print(f"Versão do MongoDB: {client.server_info()['version']}")
            return True
        except Exception as e:
            print(f"Erro ao conectar ao MongoDB: {e}")
            return False

