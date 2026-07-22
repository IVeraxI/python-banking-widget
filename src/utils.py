import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def read_json_file(file_path):
    """Читает JSON-файл и возвращает список словарей с транзакциями."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error(f"Не удалось прочитать файл {file_path}: файл не найден или содержит некорректный JSON")
        return []
    if not isinstance(data, list):
        logger.error("Данные в файле {file_path} не являются списком")
        return []

    logger.info(f"Файл {file_path} успешно прочитан, найдено {len(data)} транзакций")
    return data
