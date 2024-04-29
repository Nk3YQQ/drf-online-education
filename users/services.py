import json

from config.settings import PAYMENT_DATA_PATH


def convert_payment_to_data():
    with open(PAYMENT_DATA_PATH, 'r', encoding='utf-8') as data:
        return list({'pk': item['pk'], **item['fields']} for item in json.load(data))


print(convert_payment_to_data())
