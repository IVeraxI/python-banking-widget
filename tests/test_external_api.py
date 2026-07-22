from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_to_rub_already_rub():
    transaction = {"operationAmount": {"amount": "100.5", "currency": {"code": "RUB"}}}
    assert convert_to_rub(transaction) == 100.5


@patch("src.external_api.requests.get")
def test_convert_to_rub_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 7500.0}
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "USD"}}}
    assert convert_to_rub(transaction) == 7500.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_to_rub_eur(mock_get):
    mock_get.return_value.json.return_value = {"result": 8200.0}
    transaction = {"operationAmount": {"amount": "100", "currency": {"code": "EUR"}}}
    assert convert_to_rub(transaction) == 8200.0
