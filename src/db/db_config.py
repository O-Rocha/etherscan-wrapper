import json

class DbConfig:
    __database: str = None
    __user: str = 'postgres'
    __password: str = None
    __host: str = '127.0.0.1',
    __port: str = '5432'

    def set_config(self, file_name: str):
        with open(file_name, 'r') as file:
            data = json.load(file)
            self.__database = data['database']
            self.__user = data['user'] if data['user'] != None else self.__user
            self.__password = data['password']
            self.__host = data['host'] if data['host'] != None else self.__host
            self.__port = data['port'] if data['port'] != None else self.__port

    @property
    def database (self):
        return self.__database
    
    @property
    def user (self):
        return self.__user

    @property
    def password (self):
        return self.__password

    @property
    def host (self):
        return self.__host

    @property
    def port (self):
        return self.__port

    


