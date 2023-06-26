import random
from datetime import timedelta, date
from functions.csv_functions import *
from functions.functions import *


products_list = [
    {"product_name": "apple", "price": 0.9, "expiration_date": ""},
    {"product_name": "banana", "price": 0.7, "expiration_date": ""},
    {"product_name": "melon", "price": 1, "expiration_date": ""},
    {"product_name": "kiwi", "price": 0.5, "expiration_date": ""},
    {"product_name": "dragon_fruit", "price": 1.5, "expiration_date": ""},
    {"product_name": "pineapple", "price": 0.95, "expiration_date": ""},
    {"product_name": "lemon", "price": 0.35, "expiration_date": ""},
]


def build_bought_file(
    number_of_days,
    max_products_per_day=10,
):
    for i in range(number_of_days):
        today = get_settings_data("today")
        check_if_day_is_in_report(today)
        for i in range(max_products_per_day):
            product = products_list[random.randint(0, len(products_list) - 1)]
            expiration_date = date.fromisoformat(
                get_settings_data("today")
            ) + timedelta(days=5)
            product["expiration_date"] = "{}-{}-{}".format(
                expiration_date.year, expiration_date.month, expiration_date.day
            )

            buy_product(
                product["product_name"], product["price"], product["expiration_date"]
            )
            if (i % 2) == 0:
                sell_product(product["product_name"], random.randint(1, 5), True)

        advance_time(1)
