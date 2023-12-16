from src.setings import OPERATIONS_PATH
from src.utils import read_json_file
from src.views import show_last_five_operations


def main() -> None:
    data = read_json_file(OPERATIONS_PATH)

    transactions = show_last_five_operations(data)

    for transaction in transactions:
        print(
            f"{transaction['date']} {transaction['description']}\n"
            f"{transaction.get('from', 'нет информации счет/карта')} -> {transaction['to']}\n"
            f"{transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}\n"
        )


if __name__ == "__main__":
    main()