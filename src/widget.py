from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info_string: str) -> str:
    """Функция принимает строку с типом и номером карты/счета и возвращает маскированную версию."""
    if not isinstance(info_string, str) or not info_string.strip():
        return ""
    parts = info_string.split()
    number = parts[-1]
    name = " ".join(parts[:-1])
    if "счет" in name.lower():
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)
    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:
    """Преобразует строку даты из ISO-формата в формат ДД.ММ.ГГГГ."""
    date_obj = datetime.fromisoformat(date_string)

    return date_obj.strftime("%d.%m.%Y")
