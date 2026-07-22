import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction):
    """Конвертирует сумму транзакции в рубли."""
    amount = float(transaction["operationAmount"]["amount"])
    currency_code = transaction["operationAmount"]["currency"]["code"]

    if currency_code == "RUB":
        return amount
    api_key = os.getenv("API_KEY")
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": api_key}
    params = {"amount": amount, "from": currency_code, "to": "RUB"}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return float(data["result"])
