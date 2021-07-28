from dataclasses import dataclass

@dataclass(frozen=True)
class Transaction:
    from_add: str 
    to_add: str
    value: str
    contractAddress: str
    isError: str
    errCode: str
    timeStamp: int
    hash: str
    blockNumber: int = 0
    blockHash: str = ""
    gas: int = 0
    gasUsed: int = 0
    confirmations: int = 0
    input: str = ""
    