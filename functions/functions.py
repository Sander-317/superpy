from functions.csv_functions import *
from collections import Counter
from datetime import datetime
from rich.table import Table
from rich.console import Console


def get_product_list(product_data):
    product_data = product_data
    product_list = []
    for i in product_data:
        product_list.append((i["product_name"]))
    return product_list


def get_dict_of_products(product_data, unique_product_list):
    new_dict = {}
    for unique_product in unique_product_list:
        product_list = []
        for product in product_data:
            if product["product_name"] == unique_product:
                product_list.append(product)
        new_dict[unique_product] = product_list

    return new_dict


def get_average_price_dict(product_dict):
    # print(product_dict["orange"])
    price_dict = {}
    for product in product_dict:
        # print(product_dict[product])
        total_price = 0
        for i in product_dict[product]:
            # print("KIJK HIER ", i)
            total_price = float(i["price"]) + total_price
        price_dict[product] = round(total_price / len(product_dict[product]), 2)

    # print(price_dict)
    return price_dict


def get_unique_expiration_dates(dict):
    expiration_date_list = []
    for i in dict:
        expiration_date_list.append(i["expiration_date"])

    new_list = list(set(expiration_date_list))

    sorted_new_list = sort_dates(new_list)

    return sorted_new_list


def sort_dates(dates):
    def date_key(date_string):
        return datetime.strptime(date_string, "%Y-%m-%d")

    return sorted(dates, key=date_key)


def get_inventory_table(product_dict, average_price_dict):
    table = Table(title="inventory")
    table.add_column("name")
    table.add_column("count")
    table.add_column("price")
    table.add_column("expiration date")
    for product in product_dict:
        expiration_dates = get_unique_expiration_dates(product_dict[product])
        for date in expiration_dates:
            product_list_by_day = []
            for i in product_dict[product]:
                if i["expiration_date"] == date:
                    product_list_by_day.append(i)
                continue
            table.add_row(
                product_list_by_day[0]["product_name"],
                str(len(product_list_by_day)),
                str(average_price_dict[product]),
                date,
            )

    console = Console()
    console.print(table)


def get_bought_id(product_name, product_dict):
    if product_name in product_dict.keys():
        print(product_dict["apple"][0])
        # return product_dict[product_name][0]["id"]
    else:
        print("product not in stock")
    # print(product_dict.keys())
    # print(product_dict["apple"][0])
    # print(product_dict["apple"][0]["id"])
    return product_name
