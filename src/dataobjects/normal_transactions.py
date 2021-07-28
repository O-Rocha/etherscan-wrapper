from dataclasses import dataclass
from src.dataobjects.transactions import Transaction

@dataclass
class NormalTransaction(Transaction):
    nonce: int = 0
    transactionIndex: str = ""
    txreceipt_status: str = ""
    cumulativeGasUsed: int = 0
    confirmations: int = 0
    