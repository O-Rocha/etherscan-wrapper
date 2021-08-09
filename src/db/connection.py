import psycopg2

from .db_config import DbConfig


def open_conn(config: DbConfig) -> psycopg2.connect.__class__:
    return psycopg2.connect(
        database=config.database,
        user=config.user,
        password=config.password,
        host=config.host,
        port=config.port,
    )


def close_conn(connection: psycopg2.connect.__class__):
    connection.close()


def insert_transaction(connection: psycopg2.connect.__class__, tx: dict, internal: bool):
    cursor = connection.cursor()
    hash = validade_input(tx.get("hash")) if tx.get("hash") != None else None
    ts = int(validade_input(tx.get("timeStamp"))) if tx.get("timeStamp") != None else None 
    af = validade_input(tx.get("from")) if tx.get("from") != None else None
    at = validade_input(tx.get("to")) if tx.get("to") != None else None
    value = int(validade_input(tx.get("value"))) if tx.get("value") != None else None
    gas = int(validade_input(tx.get("gas"))) if tx.get("gas") != None else None
    gu = int(validade_input(tx.get("gasUsed"))) if tx.get("gasUsed") != None else None
    ie = bool(int(validade_input(tx.get("isError")))) if tx.get("isError") != None else None
    trs = validade_input(tx.get("txreceipt_status")) if tx.get("txreceipt_status") != None else None 
    cgu = int(validade_input(tx.get("cumulativeGasUsed"))) if tx.get("cumulativeGasUsed") != None else None
    type = validade_input(tx.get("type")) if tx.get("type") != None else None
    ti = validade_input(tx.get("traceId")) if tx.get("traceId") != None else None
    ec = validade_input(tx.get("errcode")) if tx.get("errcode") != None else None

    try:
        cursor.execute(
            "INSERT INTO transactions (hash, time_stamp, add_from, add_to, value, gas, gas_used, is_error, txreceipt_status, cumulative_gas_used, internal, type, trace_id, errcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [hash, ts, af, at, value, gas, gu, ie, trs, cgu, internal, type, ti, ec],
        )
    except:
        print("error on calling postgres lol")
        pass

    connection.commit()

def validade_input(input: str) -> str:
    return input
