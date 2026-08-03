from unittest.mock import patch

import pandas as pd

from src.csv_excel_reader import read_csv_file, read_excel_file


@patch("src.csv_excel_reader.pd.read_csv")
def test_read_csv_file(mock_read_csv):
    mock_df = pd.DataFrame([{"id":1, "amount":100}])
    mock_read_csv.return_value = mock_df

    result = read_csv_file("fake_path.csv")

    assert result == [{"id":1, "amount":100}]
    mock_read_csv.assert_called_once_with("fake_path.csv", sep=";")


@patch("src.csv_excel_reader.pd.read_excel")
def test_read_excel_file(mock_read_excel):
    mock_df = pd.DataFrame([{"id":1, "amount":100}])
    mock_read_excel.return_value = mock_df

    result = read_excel_file("fake_path.xlsx")

    assert result == [{"id":1, "amount":100}]
    mock_read_excel.assert_called_once_with("fake_path.xlsx")
