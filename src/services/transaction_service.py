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

    def get_transactions(self) -> list:
        response = []
        if (self.__config_mode == 'account'):
            response = requests.get(REQUEST_BUILDER.transaction_request(self.service_config)).json()[self.__ETHERSCAN_TXLIST]
        else:
            raise Exception('Error on api configuration: config not on account module')
        return response
    
    def get_internal_transactions(self) -> list:
        temp = self.service_config.action
        self.service_config.set_action('txlistinternal')
        response = self.get_transactions()
        self.service_config.set_action(temp)
        return response