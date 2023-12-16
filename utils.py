import json
from datetime import datetime


def read_json_file(path: str) -> list[dict]:
    """
    Функция чтения JSON файла
    :param path: str путь
    :return: list[dict] список со словарями или пустой список
    """
    with open(path, encoding='utf-8') as json_file:
        data = json.load(json_file)
        if isinstance(data, list):
            return data
        else:
            return []


def get_mask_the_bankcard(card_number: str) -> str:
    """
    Функция принимает номер банковской карты,
    возвращает замаскированый номер карты.
    """

    card_number = "".join(filter(str.isdigit, card_number))
    if len(card_number) != 16:
        return "Не верный номер карты"

    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"

    return masked_number


def get_mask_the_bank_account(account_number: str) -> str:
    """
    Функция принимает номер банковского счета,
    возвращает замаскированый номер счета.
    """

    account_number = "".join(filter(str.isdigit, account_number))
    if len(account_number) != 20:
        return "Не верный номер счета"

    masked_number = f"**{account_number[-4:]}"

    return masked_number


def get_mask_bankcard_account(number_name: str) -> str:
    """
    Принимает на вход строку информацией тип карты/счета и номер карты/счета
    :return: возвращает эту строку с замаскированным номером карты/счета.
    """

    split_number_name = number_name.split()

    if "Счет" in split_number_name:
        mask_bank_account = get_mask_the_bank_account(split_number_name[-1])
        return ' '.join(split_number_name[:-1]) + " " + mask_bank_account
    else:
        mask_bankcard = get_mask_the_bankcard(split_number_name[-1])
        return ' '.join(split_number_name[:-1]) + " " + mask_bankcard


def convert_date(date_string: str) -> str:
    """
    Принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    :return: возвращает строку с датой в виде "11.07.2018"
    """

    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date