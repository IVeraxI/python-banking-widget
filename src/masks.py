import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты в виде строки и возвращает её маску."""
    if len(card_number) != 16:
        logger.error(f"Неверная длина номера карты: {len(card_number)} символов")
        return "Ошибка: Неверная длина номера карты"

    masked = card_number[:6] + "******" + card_number[-4:]
    logger.info("Номер карты успешно замаскирован")
    return f"{masked[:4]} {masked[4:8]} {masked[8:12]} {masked[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета в виде строки и возвращает его маску."""
    if len(account_number) < 4:
        logger.error(f"Неверная длина номера счета: {len(account_number)} символов")
        return "Ошибка: Неверная длина номера счета"

    logger.info("Номер счета успешно замаскирован")
    return "**" + account_number[-4:]
