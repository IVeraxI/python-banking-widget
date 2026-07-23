import pandas as pd


def read_csv_file(file_path):
    """Читает CSV-файл с транзакциями и возвращает список словарей."""
    df = pd.read_csv(file_path, sep=";")
    return df.to_dict(orient="records")

def read_excel_file(file_path):
    """Читает Excel-файл с транзакциями и возвращает список словарей."""
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")