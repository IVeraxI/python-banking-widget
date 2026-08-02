from src.csv_excel_reader import read_csv_file, read_excel_file
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.utils import read_json_file
from src.widget import get_date, mask_account_card


def print_transaction(transaction: dict) -> None:
    """Печатает одну транзакцию в требуемом формате."""
    date = get_date(transaction.get("date", ""))
    description = transaction.get("description", "")

    if transaction.get("from"):
        accounts_line = f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}"
    else:
        accounts_line = mask_account_card(transaction["to", ""])

    amount = transaction["operationAmount"]["amount"]
    currency_name = transaction["operationAmount"]["currency"]["name"]

    print(f"{date} -> {description}")
    print(accounts_line)
    print(f"Сумма: {amount} {currency_name}")
    print()


def main() -> None:
    """Основная функция для работы с банковскими транзакциями через консоль."""
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")
    choice = input("Пользователь: ")

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        data = read_json_file("data/operations.json")
    elif choice == "2":
        print("Программа: Для обработки выбран CSV-файл.")
        data = read_csv_file("data/transactions.csv")
    elif choice == "3":
        print("Программа: Для обработки выбран XLSX-файл.")
        data = read_excel_file("data/transactions_excel.xlsx")
    else:
        print("Программа: Некорректный выбор.")
        return

    valid_statuses = ("EXECUTED", "CANCELED", "PENDING")
    while True:
        print("Программа: Введите статус, по которому необходимо выполнить фильтрацию.")
        print(f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}")
        status = input("Пользователь: ").upper()
        if status in valid_statuses:
            break
        print(f'Программа: Статус операции "{status}" недоступен.')

    data = filter_by_state(data, status)
    print(f'Программа: Операции отфильтрованы по статусу "{status}"')

    if input("Программа: Отсортировать операции по дате? Да/Нет\nПользователь: ").lower() == "да":
        order = input("Программа: Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        data = sort_by_date(data, reverse=(order == "по убыванию"))
    if input("Программа: Выводить только рублевые транзакции? Да/Нет\nПользователь: ").lower() == "да":
        data = [t for t in data if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]

    if input("Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\nПользователь: ").lower() == "да":
        word = input("Программа: Введите слово для поиска.\nПользователь: ")
        data = process_bank_search(data, word)

    print("Программа: Распечатываю итоговый список транзакций...")
    print("Программа:")

    if not data:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(data)}")
    for transaction in data:
        print_transaction(transaction)


if __name__ == "__main__":
    main()
