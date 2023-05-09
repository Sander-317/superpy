from functions.csv_functions import *
from collections import Counter


def get_product_list(product_data):
    product_data = product_data
    product_list = []
    for i in product_data:
        product_list.append((i["product_name"]))
    return product_list


def get_dict_of_products(product_data, unique_product_list):
    new_dict = {}
    for unique_product in unique_product_list:
        # print("unique product = ", unique_product)
        product_list = []
        for product in product_data:
            # print(product["product_name"])
            if product["product_name"] == unique_product:
                product_list.append(product)
        new_dict[unique_product] = product_list
    # print(new_dict["orange"])
    return new_dict


def get_average_price_dict(product_dict):
    # print(product_dict["orange"])
    price_dict = {}
    for product in product_dict:
        # print(product_dict[product])
        total_price = 0
        for i in product_dict[product]:
            # print(i["price"])
            total_price = float(i["price"]) + total_price
        price_dict[product] = round(total_price / len(product_dict[product]), 2)

    print(price_dict)
    return price_dict


def get_inventory():
    product_data = get_bought_data()
    product_list = get_product_list(product_data)
    unique_product_list = sorted(set(product_list))
    count = Counter(product_list)
    product_dict = get_dict_of_products(product_data, unique_product_list)
    average_price_dict = get_average_price_dict(product_dict)
    # print(Counter(product_list))
    # test = Counter(product_dict["banana"])
    # print(product_dict["banana"])
    # print(test)
    # print(count)
    # print(count["orange"])
    # print(count["price"])

    table = Table(title="inventory")
    table.add_column("name")
    table.add_column("count")
    table.add_column("price")
    table.add_column("expiration date")
    for product in unique_product_list:
        print(product)
        table.add_row(
            product,
            str(count[product]),
            str(average_price_dict[product]),
            # (product["expiration_date"]),
        )

    # print(unique_product_list)
    # print(product_list)
    console = Console()
    console.print(table)
