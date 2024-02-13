from bson import ObjectId
class TeacherCollection:
    def __init__(self):
        self.id: str
        self.nome: str
        self.cpf: str
        self.curso: str
