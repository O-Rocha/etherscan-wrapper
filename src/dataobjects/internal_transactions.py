from dataclasses import dataclass
from transactions import Transaction

@dataclass
class InternalTransaction(Transaction):
    tx_type: str = ""
    trace_id: str = ""
    