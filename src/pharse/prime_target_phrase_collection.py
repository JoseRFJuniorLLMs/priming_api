from bson import ObjectId
from typing import List


class PrimeTargetPhraseCollection:
    def __init__(self):
        self.id: str
        self.prime: str
        self.target: str
        self.phrase: List[str]
        self.url: List[str]
        self.imagem: List[str]
