import pytest
from src.processing import filter_by_state, sort_by_date
from src.processing import process_bank_operations, process_bank_search


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2023-05-15T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-20T00:00:00.000000"}
    ]


@pytest.fixture
def transactions():
    return [
        {"id": 1, "description": "Перевод организации"},
        {"id": 2, "description": "Открытие вклада"},
        {"id": 3, "description": "Перевод со счета на счет"},
        {"id": 4, "description": "Перевод организации"},
    ]


@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 1),
    ("PENDING", 0),
])
def test_filter_by_state(operations, state, expected_count):
    result = filter_by_state(operations, state)
    assert len(result) == expected_count


def test_sort_by_date_descending(operations):
    result = sort_by_date(operations)
    assert result[0]["date"] == "2024-03-20T00:00:00.000000"


def test_sort_by_date_ascending(operations):
    result = sort_by_date(operations, reverse=False)
    assert result[0]["date"] == "2023-05-15T00:00:00.000000"


def test_process_bank_search_found(transactions):
    result = process_bank_search(transactions, "перевод")
    assert len(result) > 0
    assert all("перевод" in t["description"].lower() for t in result)


def test_process_bank_search_case_insensitive(transactions):
    result_lower = process_bank_search(transactions, "перевод")
    result_upper = process_bank_search(transactions, "ПЕРЕВОД")
    assert result_lower == result_upper


def test_process_bank_search_not_found(transactions):
    result = process_bank_search(transactions, "несуществующий текст 12345")
    assert result == []


def test_process_bank_search_missing_description():
    data = [{}, {"description": "Перевод организации"}]
    result = process_bank_search(data, "перевод")
    assert len(result) == 1


def test_process_bank_operations(transactions):
    counts = process_bank_operations(transactions, ["Перевод организации", "Открытие вклада"])
    assert isinstance(counts, dict)
    assert "Перевод организации" in counts
    assert "Открытие вклада" in counts


def test_process_bank_operations_category_not_present(transactions):
    counts = process_bank_operations(transactions, ["Несуществующая категория"])
    assert counts["Несуществующая категория"] == 0
