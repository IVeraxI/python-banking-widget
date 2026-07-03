import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {"id": 1, "description": "Перевод организации",
         "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 2, "description": "Перевод со счета на счет",
         "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 3, "description": "Перевод со счета на счет",
         "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 4, "description": "Перевод с карты на карту",
         "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 5, "description": "Перевод организации",
         "operationAmount": {"currency": {"code": "RUB"}}},
    ]


@pytest.mark.parametrize("currency, expected_count", [
    ("USD", 3),
    ("RUB", 2),
    ("EUR", 0),
])
def test_filter_by_currency(transactions, currency, expected_count):
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count


def test_filter_bycurrency_empty_list():
    assert list(filter_by_currency([], "USD")) == []


def test_transaction_descriptions(transactions):
    gen = transaction_descriptions(transactions)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"


@pytest.mark.parametrize("start, stop, expected_first, expected_last, expected_count", [
    (1, 5, "0000 0000 0000 0001", "0000 0000 0000 0005", 5),
    (10, 12, "0000 0000 0000 0010", "0000 0000 0000 0012", 3),
])
def test_card_number_generators(start, stop, expected_first, expected_last, expected_count):
    result = list(card_number_generator(start, stop))
    assert result[0] == expected_first
    assert result[-1] == expected_last
    assert len(result) == expected_count
