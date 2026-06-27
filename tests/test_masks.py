import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567890123456", "1234 56** **** 3456"),
    ("1234", "Ошибка: Неверная длина номера карты"),
    ("12345678901234567", "Ошибка: Неверная длина номера карты"),
])
def test_get_mask_card_number(card, expected):
    assert get_mask_card_number(card) == expected


@pytest.mark.parametrize("account, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678", "**5678"),
    ("123", "Ошибка: Неверная длина номера счета"),
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
