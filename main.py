from src.common.api_config import ApiConfig
from src.common import build_request_string

teste = ApiConfig()
teste.set_config('api_config.json')

url = build_request_string.normal_transaction_request(teste)

print(url)
