import json

class ApiConfig:
    __base_url: str = None
    __module: str = None
    __action: str = None
    __address: str = None
    __api_key: str = None
    
    @property
    def base_url (self):
        return self.__base_url

    @property
    def module (self):
        return self.__module

    @property
    def action (self):
        return self.__action

    @property
    def address (self):
        return self.__address

    @property
    def api_key (self):
        return self.__api_key

    def set_config(self, file_name: str):
        with open(file_name, 'r') as file:
            data = json.load(file)
            self.__base_url = data['base_url']
            self.__module = data['module']
            self.__action = data['action']
            self.__address = data['address']
            self.__api_key = data['api_key']

    def __repr__(self) -> str:
        return( 
            f'URL    : {self.base_url}\n'
            f'METHOD : {self.module}\n'
            f'ACTION : {self.action}\n'
            f'ADDRESS: {self.address}'
        )
    
    def set_action(self, action: str):
        self.__action = action
    
    def set_address(self, address: str):
        self.__address = address
    
    def set_api_key(self, api_key: str):
        self.__api_key = api_key
    
    
 