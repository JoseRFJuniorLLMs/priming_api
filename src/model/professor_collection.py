from bson import ObjectId
class ProfessorCollection:
    def __init__(self):
        self.id: str
        self.nome: str
        self.cpf: str
        self.curso: str
