# from functions.csv_functions import *
# import csv_functions as csvf
# from functions import csv_functions
from . import csv_functions as csv_functions


# from csv_functions import *
from collections import Counter
from datetime import datetime
from rich.table import Table
from rich.console import Console


def get_product_list(product_data):
    product_list = []
    for i in product_data:
        product_list.append((i["product_name"]))
    return product_list


def get_dict_of_products(product_data, unique_product_list, sold_products_id_list):
    new_dict = {}
    for unique_product in unique_product_list:
        product_list = []
        for product in product_data:
            if product["product_name"] == unique_product:
                if product["id"] not in sold_products_id_list:
                    product_list.append(product)
        new_dict[unique_product] = product_list

    return new_dict


def get_average_price_dict(product_dict):
    price_dict = {}
    for product in product_dict:
        total_price = 0
        for i in product_dict[product]:
            total_price = float(i["price"]) + total_price
        if len(product_dict[product]) > 1:
            price_dict[product] = round(total_price / len(product_dict[product]), 2)
        else:
            price_dict[product] = round(total_price, 2)
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


def get_inventory_table(product_dict, average_price_dict, sold_products_id_list, today):
    table = Table(title="inventory")
    table.add_column("name")
    table.add_column("count")
    table.add_column("price")
    table.add_column("expiration date")

    for product in product_dict:
        expiration_dates = get_unique_expiration_dates(product_dict[product])
        for date in expiration_dates:
            product_list_by_day = []
            for product_in_dict in product_dict[product]:
                if datetime.strptime(
                    product_in_dict["expiration_date"], "%Y-%m-%d"
                ) >= datetime.strptime(today, "%Y-%m-%d"):
                    if product_in_dict["id"] not in sold_products_id_list:
                        if product_in_dict["expiration_date"] == date:
                            product_list_by_day.append(product_in_dict)
                    else:
                        continue
                else:
                    # TODO: add sell function once you made hem to add spoiled products to cost in the report
                    continue
            if product_list_by_day != []:
                table.add_row(
                    product_list_by_day[0]["product_name"],
                    str(len(product_list_by_day)),
                    str(average_price_dict[product]),
                    date,
                )

    console = Console()
    console.print(table)


def get_bought_id(product_name, product_dict, sold_products_id_list):
    if product_name in product_dict.keys():
        for product in product_dict[product_name]:
            if product["id"] != "":
                if product["id"] not in sold_products_id_list:
                    return product["id"]
            else:
                print("product not in stock")

    else:
        print("product not in stock")


def get_report_dates(report_data):
    new_list = []
    for date in report_data:
        new_list.append(date["date"])
    return new_list


def create_report_data(action, buy_date, buy_price, report_data):
    for date in report_data:
        if date["date"] == buy_date:
            if action == "buy":
                date.update({"cost": str(int(date["cost"]) + int(buy_price))})
                break
            elif action == "sell":
                date.update({"revenue": str(int(date["revenue"]) + int(buy_price))})
                break
            date.update({"profit": str(int(date["revenue"]) - int(date["cost"]))})

    csv_functions.write_to_report_csv(report_data)
    create_report_table(report_data)
    # print(data)


# def create_report_data(action, buy_date, buy_price, report_data):
#     if action == "buy":
#         for date in report_data:
#             if date["date"] == buy_date:
#                 date.update({"cost": str(int(date["cost"]) + int(buy_price))})
#                 date.update({"profit": str(int(date["revenue"]) - int(date["cost"]))})
#                 break
#     if action == "sell":
#         for date in report_data:
#             if date["date"] == buy_date:
#                 date.update({"revenue": str(int(date["revenue"]) + int(buy_price))})
#                 date.update({"profit": str(int(date["revenue"]) - int(date["cost"]))})
#                 break

#     csv_functions.write_to_report_csv(report_data)
#     create_report_table(report_data)
#     # print(data)


def create_report_table(report_data):
    table = Table(title="report")
    table.add_column("date")
    table.add_column("cost")
    table.add_column("revenue")
    table.add_column("profit")

    for data in report_data:
        table.add_row(data["date"], data["cost"], data["revenue"], data["profit"])
    console = Console()
    console.print(table)


def check_if_day_is_in_report(today):
    report_data = csv_functions.get_report_data()
    report_data_dates = csv_functions.get_report_dates(report_data)

    if today not in report_data_dates:
        csv_functions.add_report_data(
            csv_functions.get_id(),
            today,
            0,
            0,
        )
