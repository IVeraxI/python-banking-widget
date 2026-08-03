import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Ищет операции, в описании которых встречается заданная строка."""
    pattern = re.compile(search, re.IGNORECASE)
    return [transaction for transaction in data if pattern.search(transaction.get("description", ""))]


def process_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """Подсчитывает количество операций по каждой категории из description."""
    descriptions = [transaction.get("description", "") for transaction in data]
    counted = Counter(descriptions)
    return {category: counted.get(category, 0) for category in categories}


def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтруем операции по их статусу."""
    filtered_operations = []
    for op in operations:
        if op.get("state") == state:
            filtered_operations.append(op)
    return filtered_operations


def get_date_key(op: dict) -> str:
    """Вспомогательная функция для получения даты."""
    return str(op.get("date", ""))


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортируем операции по дате."""
    sorted_operations = sorted(operations, key=get_date_key, reverse=reverse)
    return sorted_operations
