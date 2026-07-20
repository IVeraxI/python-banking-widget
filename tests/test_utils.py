import json
from unittest.mock import mock_open, patch

from src.utils import read_json_file


def test_read_json_file_success():
    test_data = [{"id": 1, "amount": "100"}]
    mock_data = json.dumps(test_data)
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("fake_path.json")
    assert result == test_data


def test_read_json_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_json_file("missing.json")
    assert result == []


def test_read_json_file_empty():
    with patch("builtins.open", mock_open(read_data="")):
        result = read_json_file("empty.json")
    assert result == []


def test_read_json_file_not_a_list():
    mock_data = json.dumps({"key": "value"})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        result = read_json_file("not_list.json")
    assert result == []
