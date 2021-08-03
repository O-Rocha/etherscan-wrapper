import requests

from src.common import REQUEST_BUILDER
from src.common.api_config import ApiConfig

class ContractService:
    __ETHERSCAN_SOURCECODE: str = 'SourceCode'
    __config_mode: str = None
    service_config: ApiConfig = None

    def __init__(self, config: ApiConfig) -> None:
        self.service_config = config
        self.__config_mode = config.module
    
    def get_source_code(self) -> str:
        response = ''
        if (self.__config_mode == 'contract'):
            response = requests.get(REQUEST_BUILDER.normal_request(self.service_config)).json()['result'][0][self.__ETHERSCAN_SOURCECODE]
        else:
            raise Exception('Error on api configuration: config not on contract module')
        return response