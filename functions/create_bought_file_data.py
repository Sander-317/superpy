# from datetime import date
import random
from rich import print

# # from settings import *
# from functions.csv_functions import *
from functions.csv_functions import *

# from csv_functions import *

# from functions.functions import *

# from functions import *

# from classes.Product import *

products_list = [
    {"product_name": "apple", "price": 0.9, "expiration_days": 5},
    {"product_name": "banana", "price": 0.7, "expiration_days": 5},
    {"product_name": "melon", "price": 1, "expiration_days": 5},
    {"product_name": "kiwi", "price": 0.5, "expiration_days": 5},
    {"product_name": "dragon_fruit", "price": 1.5, "expiration_days": 5},
    {"product_name": "pineapple", "price": 0.95, "expiration_days": 5},
    {"product_name": "lemon", "price": 0.35, "expiration_days": 5},
    {"product_name": "", "price": 2, "expiration_days": 5},
]

# print(products_list[0]["product_name"])
# print("random number 1", products_list[random.randint(0, len(products_list))])
# print("random number 2", products_list[random.randint(0, len(products_list))])
# print("random number 3", products_list[random.randint(0, len(products_list))])
# # Buy_product(get_id(), product_name, price, expiration_date).buy()


def build_bought_file(
    number_of_days,
    products_per_day,
):
    today = get_today()
    print(today)
    for i in range(number_of_days):
        print("day", i + 1)
        for i in range(products_per_day):
            print(products_list[random.randint(0, len(products_list) - 1)])


# build_bought_file(5, 5)
