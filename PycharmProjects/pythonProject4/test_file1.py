import json
import pytest
from file1 import load_operations, mask_card_number, mask_account_number, print_last_5_executed_operations

@pytest.fixture
def sample_operations_data():
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2023-01-01T12:00:00",
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Transaction 1",
            "from": "Card 1234 5678",
            "to": "Account 123456789"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2023-01-02T12:00:00",
            "operationAmount": {
                "amount": "200.00",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Transaction 2",
            "from": "Card 9876 5432",
            "to": "Account 987654321"
        },
        # Добавьте другие операции здесь

    ]

def test_load_operations(sample_operations_data, tmp_path):
    # Создаем временный файл с данными для тестирования
    test_file = tmp_path / "test_operations.json"
    test_file.write_text(json.dumps(sample_operations_data))

    # Проверяем, что данные успешно загружаются из файла
    operations_data = load_operations(test_file)
    assert operations_data == sample_operations_data

def test_mask_card_number():
    assert mask_card_number('1234567890123456') == '1234 **** 3456'
    assert mask_card_number('') == ''

def test_mask_account_number():
    assert mask_account_number('1234567890') == '**7890'
    assert mask_account_number('') == ''

def test_print_last_5_executed_operations(sample_operations_data, capsys):
    operations_data = sample_operations_data
    print_last_5_executed_operations(operations_data)
    captured = capsys.readouterr()
    # Добавьте здесь проверки для утверждений о выводе



    # Запускаем тестирование с дополнительными данными
    assert len(captured.out.strip().split('\n')) == 4 * len(operations_data)

def test_empty_operations_data(capsys):
    # Проверяем, что функция вывода работает корректно, если список операций пустой
    print_last_5_executed_operations([])
    captured = capsys.readouterr()
    assert captured.out.strip() == ''

if __name__ == "__main__":
    pytest.main([__file__])
