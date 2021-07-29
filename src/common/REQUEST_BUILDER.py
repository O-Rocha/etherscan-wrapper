from .api_config import ApiConfig

def normal_transaction_request(config: ApiConfig):
    return(
        f'{config.base_url}'
        f'?module={config.module}&action={config.action}'
        f'&address={config.address}&apiKey={config.api_key}'
    )