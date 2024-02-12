from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel


class OID(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(str(v))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")


# Exemplo de uso
class MyModel(BaseModel):
    id: OID


# Teste
try:
    data = {"id": "123"}  # Simulando um ID inválido
    model = MyModel(**data)
    print(model)
except ValueError as e:
    print(e)  # Output: Not a valid ObjectId
