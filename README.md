# Jetton Rate API

Этот проект представляет простой асинхронный клиент для получения курсов криптовалют с использованием TON API. Клиент позволяет извлекать обменный курс между конкретными токенами и валютами.

## Особенности

- Асинхронные запросы с использованием aiohttp
- Удобный интерфейс для получения курсов
- Поддержка нескольких токенов и валют

## Пример кода
```python
from tonapi import TonAPI
api = TonAPI()

exchange_rate_tonapi = api.get_rate("USD", "TON")
different = api.get_diff("USD", "TON", "24h")
exchange_rate_stonfi = get_rate_by_stonfi("TON")
print(exchange_rate_tonapi, different, exchange_rate_stonfi)
```

## Установка

1. Клонируйте репозиторий: `git clone https://github.com/vladdintov/TonAPI.git`
2. Установите зависимости: `poetry install`
3. Запустите приложение: `python main.py`

