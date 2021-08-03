import requests

from src.common import REQUEST_BUILDER
from src.common.api_config import ApiConfig
# from src.dataobjects.normal_transactions import NormalTransaction

class TransactionService:
    __ETHERSCAN_TXLIST: str = 'result'
    __config_mode: str = None
    service_config: ApiConfig = None

    def __init__(self, config: ApiConfig) -> None:
        self.service_config = config
        self.__config_mode = config.module

    def get_normal_transactions(self) -> list:
        response = []
        if (self.__config_mode == 'account'):
            response = requests.get(REQUEST_BUILDER.normal_request(self.service_config)).json()[self.__ETHERSCAN_TXLIST]
        else:
            raise Exception('Error on api configuration: config not on contract module')
        return response

    def get_internal_transactions(self) -> list:
        response = []
        if (self.__config_mode == 'account'):
            response = requests.get(REQUEST_BUILDER.internal_transaction_request(self.service_config)).json()[self.__ETHERSCAN_TXLIST]
        else:
            raise Exception('Error on api configuration: config not on contract module')
        return response