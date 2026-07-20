import json

def read_json_file(file_path):
    """Читает JSON-файл и возвращает список словарей с транзакциями."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    if not isinstance(data, list):
        return []
    return data
