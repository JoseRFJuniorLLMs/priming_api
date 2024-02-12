from bson import ObjectId
from typing import List


class PrimeTargetYoutubeCollection:
    def __init__(self):
        self.id: str
        self.prime: str
        self.target: str
        self.url: List[str]