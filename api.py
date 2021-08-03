from src.common import file_service as fileWriter
from src.common.api_config import ApiConfig
from src.services.transaction_service import TransactionService
from src.services.contract_service import ContractService

config = ApiConfig()
config.set_config('api-config.json')

service = TransactionService(config)

txlist = service.get_normal_transactions()
txlistinternal = service.get_internal_transactions()

fileWriter.make_file(txlist, f'../{config.address}_tx.txt')

fileWriter.make_file(txlistinternal, f'../{config.address}_txinternal.txt')

# service = ContractService(config)

# code = service.get_source_code()

# fileWriter.write_source_code(code, f'../{config.address}_sourcecode.sol')