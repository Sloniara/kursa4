import json

def load_operations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def mask_card_number(card_number):
    return f"{card_number[:4]} {'*'*6} {card_number[-4:]}" if card_number else ''

def mask_account_number(account_number):
    return f"**{account_number[-4:]}" if account_number else ''

def print_last_5_executed_operations(operations_data):
    executed_operations = [op for op in operations_data if op.get('state') == 'EXECUTED']
    sorted_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    for op in sorted_operations:
        date = op['date'][:10]  # Извлекаем только дату
        description = op['description']
        source = mask_card_number(op.get('from', '').split()[1]) if op.get('from') else ''  # Получаем только номер карты, если поле 'from' не пустое
        destination = mask_account_number(op['to'].split()[-1]) if op.get('to') else ''  # Получаем только последние 4 цифры счета, если поле 'to' не пустое
        amount = op['operationAmount']['amount']
        currency = op['operationAmount']['currency']['name']  # Получаем только имя валюты

        print(f"{date} {description}")
        print(f"{source} -> {destination}")
        print(f"{amount} {currency}")
        print("-" * 40)  # Добавляем разделительную линию

if __name__ == "__main__":
    operations_data = load_operations('operations.json')
    print_last_5_executed_operations(operations_data)
