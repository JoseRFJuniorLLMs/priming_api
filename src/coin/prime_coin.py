from datetime import datetime
from typing import List

from bson import ObjectId
from datetime import datetime
from typing import List


class PrimeCoin:
    def __init__(self):
        self.primecoinValue: float
        self.bitcoinValue: float
        self.lastUpdated: datetime
        self.ownerId: str
        self.transactionHistory: List[str]
        self.initialBalance: float
        self.publicKey: str
        self.privateKey: str
        self.name: str
        self.description: str
        self.creationDate: datetime
        self.issuer: str