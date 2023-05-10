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
        # print(i)
    # print(set(expiration_date_list))
    return set(expiration_date_list)


def sort_list_by_expiration_date(dictionary):
    new_dict = {}
    for product in dictionary:
        # print("TEST", dictionary[product])
        expiration_dates = get_unique_expiration_dates(dictionary[product])
        product_list = dictionary[product]
        # print(product)
        print(expiration_dates)
        product_list_by_product = {}
        for date in expiration_dates:
            product_list_by_day = []
            for product in product_list:
                if product["expiration_date"] == date:
                    # print(product)
                    product_list_by_day.append(product)
                else:
                    continue
            product_list_by_product[product["expiration_date"]] = product_list_by_day
            # print("product list by day", product_list_by_day)
        # if date == product["expiration_date"]:
        # print(product)
        # print(date)
        new_dict["product_name"] = product_list_by_product
        # print(product_list_by_product)
    print(new_dict.keys)
    return new_dict


def get_inventory():
    product_data = get_bought_data()
    product_list = get_product_list(product_data)
    unique_product_list = sorted(set(product_list))
    count = Counter(product_list)
    product_dict = get_dict_of_products(product_data, unique_product_list)
    average_price_dict = get_average_price_dict(product_dict)
    product_dict_sorted_by_expiration_date = sort_list_by_expiration_date(product_dict)
    print(product_dict_sorted_by_expiration_date)
    # print("PRODUCT DICT", product_dict["apple"])
    # get_unique_expiration_dates(product_dict["apple"])
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
    table.add_column("price", style="red")
    table.add_column("expiration date")
    # for product in product_dict:
    #     print("TEST", product_dict[product])
    #     expiration_dates = get_unique_expiration_dates(product_dict[product])
    #     print(expiration_dates)
    # for expiration_date in expiration_dates:
    #     print(expiration_date)

    # for product in unique_product_list:
    #     print(product)
    #     # print("TEST", product[0])
    #     table.add_row(
    #         product,
    #         str(count[product]),
    #         str(average_price_dict[product]),
    #         # product["expiration_date"],
    #     )

    # print(unique_product_list)
    # print(product_list)
    # console = Console()
    # console.print(table)
