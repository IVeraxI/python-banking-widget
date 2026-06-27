import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_date, expected",[
    ("Visa Classic 7000792289606361", "Visa Classic 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
])
def test_mask_account_card(input_date, expected):
    assert mask_account_card(input_date) == expected


@pytest.mark.parametrize("input_date, expected",[
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2019-12-01T00:00:00.000000", "01.12.2019"),
])
def test_get_date(input_date, expected):
    assert get_date(input_date) == expected
