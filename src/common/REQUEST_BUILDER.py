from .api_config import ApiConfig

def transaction_request(config: ApiConfig):
    return(
        f'{config.base_url}'
        f'?module={config.module}&action={config.action}'
        f'&address={config.address}&apiKey={config.api_key}'
    )

def transaction_with_pagination_request(config: ApiConfig, page: int, offset: int):
    return(
        f'{config.base_url}'
        f'?module={config.module}&action={config.action}'
        f'&address={config.address}&page={page}&Offset={offset}&apiKey={config.api_key}'
    )

def transaction_with_pagination_and_sorting_request(config: ApiConfig, page: int, offset: int, sort: str):
    #sorting can be done with asc or desc
    return(
        f'{config.base_url}'
        f'?module={config.module}&action={config.action}'
        f'&address={config.address}&page={page}&Offset={offset}&sort={sort}&apiKey={config.api_key}'
    )