from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Маскирует номер карты или счета, принимая один строковый аргумент."""
    if not info_string or not info_string.strip():
        return "Ошибка: пустой ввод"

    parts = info_string.split()

    if len(parts) < 2:
        return "Ошибка: неверный формат данных"

    number = parts[-1]

    name = " ".join(parts[:-1])

    if not number.isdigit():
        return "Ошибка: номер должен содержать только цифры"

    if "счет" in name.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует строку даты из ISO-формата в формат ДД.ММ.ГГГГ."""
    date_obj = datetime.fromisoformat(date_string)

    return date_obj.strftime("%d.%m.%Y")
