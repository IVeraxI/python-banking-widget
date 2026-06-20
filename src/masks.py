def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты в виде строки и возвращает её маску."""
    if len(card_number) != 16:
        return "Ошибка: Неверная длина номера карты"

    masked = card_number[:6] + "******" + card_number[-4:]
    return f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета в виде строки и возвращает его маску."""
    if len(account_number) < 4:
        return "Ошибка: Неверная длина номера счета"

    return "**" + account_number[-4:]
