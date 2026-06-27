import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T00:00:00.000000"},
        {"id": 2, "state": "CANCELED", "date": "2023-05-15T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2024-03-20T00:00:00.000000"}
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