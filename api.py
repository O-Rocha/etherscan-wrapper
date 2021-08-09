from src.common import file_service as fileWriter
from src.common.api_config import ApiConfig
from src.services.transaction_service import TransactionService
from src.services.contract_service import ContractService
from src.db.db_config import DbConfig
from src.db import connection

db_config = DbConfig()
db_config.set_config('db-config.json')
conn = connection.open_conn(db_config)
conn.autocommit = False

config = ApiConfig()
config.set_config('api-config.json')

service = TransactionService(config)

txlist = service.get_transactions()
txlistinternal = service.get_internal_transactions()

#insere todas as transações normais do contrato na base de dados
for tx in txlist:
    tx = dict(tx)
    connection.insert_transaction(conn, tx, False)

#insere todas as transações internas do contrato na base de dados
for tx in txlistinternal:
    tx = dict(tx)
    connection.insert_transaction(conn, tx, True)

connection.close_conn(conn)

# service = ContractService(config)
# code = service.get_source_code()
# fileWriter.write_source_code(code, f'../{config.address}_sourcecode.sol')