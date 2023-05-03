from functions.csv_functions import *
from collections import Counter


def get_inventory():
    product_data = get_bought_data()
    product_list = []
    for i in product_data:
        product_list.append((i["product_name"]))
    test = Counter(product_list)
    # print(Counter(product_list))
    print(test)
    print(test["orange"])

    unique_product_list = set(product_list)
    table = Table(title="inventory")
    table.add_column("name")
    table.add_column("count")
    table.add_column("price")
    table.add_column("expiration date")
    # for i in unique_product_list:

    # print(unique_product_list)
    # print(product_list)
    # console = Console()
    # console.print(table)
