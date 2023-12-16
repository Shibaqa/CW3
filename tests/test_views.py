import pytest

from src.views import show_last_five_operations
from tests.settings_test_views import TEST_DATA_1, TEST_DATA_2


@pytest.fixture
def transactions() -> list[dict]:
    return TEST_DATA_1


@pytest.fixture
def expected() -> list[dict]:
    return TEST_DATA_2


def test_show_last_five_operations(transactions: list[dict], expected: list[dict]) -> None:
    """
    Тест для проверки функции show_last_five_operations
    :param transactions: транзакции
    :param expected: транзакции
    :return: None
    """
    assert show_last_five_operations(transactions) == expected