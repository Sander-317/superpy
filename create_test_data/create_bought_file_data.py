import random
import datetime
from datetime import date
from functions.csv_functions import *
from classes.Product import *


products_list = [
    {"product_name": "apple", "price": 0.9, "expiration_date": ""},
    {"product_name": "banana", "price": 0.7, "expiration_date": ""},
    {"product_name": "melon", "price": 1, "expiration_date": ""},
    {"product_name": "kiwi", "price": 0.5, "expiration_date": ""},
    {"product_name": "dragon_fruit", "price": 1.5, "expiration_date": ""},
    {"product_name": "pineapple", "price": 0.95, "expiration_date": ""},
    {"product_name": "lemon", "price": 0.35, "expiration_date": ""},
]


# Buy_product(get_id(), product_name, price, expiration_date).buy()


def build_bought_file(
    number_of_days,
    max_products_per_day,
):
    # today = date.fromisoformat(get_today())

    for i in range(number_of_days):
        for i in range(random.randint(0, max_products_per_day)):
            product = products_list[random.randint(0, len(products_list) - 1)]
            # expiration_date = today + datetime.timedelta(days=5)
            expiration_date = date.fromisoformat(get_today()) + datetime.timedelta(
                days=5
            )
            product["expiration_date"] = "{}-{}-{}".format(
                expiration_date.year, expiration_date.month, expiration_date.day
            )
            # print(product)
            Buy_product(
                get_id(),
                product["product_name"],
                product["price"],
                product["expiration_date"],
            ).buy()
        # today = today + datetime.timedelta(days=1)
        advance_time(1)
