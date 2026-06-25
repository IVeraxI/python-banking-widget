def filter_by_state(operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтруем операции по их статусу."""
    filtered_operations = []
    for op in operations:
        if op.get("state") == state:
            filtered_operations.append(op)
    return filtered_operations


def get_date_key(op: dict) -> str:
    """Вспомогательная функция для получения даты."""
    return op.get("date", "")


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортируем операции по дате."""
    sorted_operations = sorted(operations, key=get_date_key, reverse=reverse)
    return sorted_operations
