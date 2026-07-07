def filter_by_currency(transactions, currency_code):
    """Фильтрует транзакции по коду валюты, возвращает итератор."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(transactions):
    """Генерирует описание каждой транзакции по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """Генерирует номера карт в заданном диапазоне в формате XXXX XXXX XXXX XXXX."""
    for number in range(start,stop + 1):
        digits = str(number).zfill(16)
        yield f"{digits[:4]} {digits[4:8]} {digits[8:12]} {digits[12:]}"