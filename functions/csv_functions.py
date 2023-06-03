import csv

# import datetime
# from datetime import date
from datetime import datetime, timedelta, date
from functions.functions import *
from rich.table import Table
from rich.console import Console


def buy_product(product_name, price, expiration_date):
    with open("data/bought.csv", "a", newline="") as new_file:
        fieldnames = [
            "id",
            "buy_date",
            "product_name",
            "price",
            "expiration_date",
        ]
        to_add = {
            "id": get_id(),
            "buy_date": get_today(),
            "product_name": product_name,
            "price": price,
            "expiration_date": expiration_date,
        }
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writerow(to_add)
        # csv_writer.writerow(
        #     {
        #         "id": get_id(),
        #         "buy_date": get_today(),
        #         "product_name": product_name,
        #         "price": price,
        #         "expiration_date": expiration_date,
        #     }
        # )
        # add_report_data(get_id(), to_add["buy_date"], to_add["price"])
    # print("new buy product function", product_name, price, expiration_date)
    # print("report data", get_report_data())
    # print("add test to report data", add_report_data("test"))
    # print("report data with test added", get_report_data())


def sell_product(product_name, price, product_dict, sold_products_id_list):
    with open("data/sold.csv", "a", newline="") as new_file:
        fieldnames = [
            "id",
            "bought_id",
            "sell_date",
            "price",
        ]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writerow(
            {
                "id": get_id(),
                "bought_id": get_bought_id(
                    product_name, product_dict, sold_products_id_list
                ),
                "sell_date": get_today(),
                "price": price,
            }
        )


def get_id():  # Walrus in function
    with open("data/id.csv", "r") as csv_id:
        csv_reader = csv.reader(csv_id)
        for row in csv_reader:
            (id := row[0])
    with open("data/id.csv", "w") as csv_id:
        csv_writer = csv.writer(csv_id)
        csv_writer.writerow(
            [
                int(id) + 1,
            ]
        )
    return id


def get_today():  # Walrus in function
    with open("data/today.csv", "r") as csv_id:
        csv_reader = csv.reader(csv_id)
        for row in csv_reader:
            (today := row[0])

    return today


def get_report_data():
    with open("data/report.csv", "r") as csv_report:
        fieldnames = ["id", "date", "cost", "revenue", "profit"]
        csv_reader = csv.DictReader(csv_report, fieldnames=fieldnames)
        # csv_reader = csv.reader(csv_report)

        new_list = []
        for row in csv_reader:
            new_list.append(
                {
                    "id": row["id"],
                    "date": row["date"],
                    "cost": row["cost"],
                    "revenue": row["revenue"],
                    "profit": row["profit"],
                }
            )
        # for row in csv_reader:
        #     new_list.append(row)
        # print("new list in get report data", new_list)
    return new_list


def add_report_data(
    id,
    date,
    cost,
    revenue,
):
    # print("get report data in add report data", get_report_data())
    report_data = get_report_data()
    new_profit = revenue - cost
    report_data.append(
        {"id": id, "date": date, "cost": cost, "revenue": revenue, "profit": new_profit}
    )
    # print(report_data)
    # print(report_data[0])
    with open(
        "data/report.csv",
        "w",
    ) as csv_report:
        fieldnames = ["id", "date", "cost", "revenue", "profit"]
        csv_writer = csv.DictWriter(csv_report, fieldnames=fieldnames)
        for row in report_data:
            csv_writer.writerow(row)


def advance_time(days):
    today = date.fromisoformat(get_today())
    new_date = today + timedelta(days=int(days))
    new_list = []
    new_list.append(new_date)
    with open("data/today.csv", "w") as csv_today:
        csv_writer = csv.writer(csv_today)
        csv_writer.writerow(new_list)
    return new_date


def get_bought_data():
    with open("data/bought.csv", "r") as new_file:
        fieldnames = ["id", "buy_date", "product_name", "price", "expiration_date"]
        csv_reader = csv.DictReader(new_file, fieldnames=fieldnames)
        product_list = []
        for row in csv_reader:
            product_list.append(
                {
                    "id": row["id"],
                    "product_name": row["product_name"],
                    "buy_date": row["buy_date"],
                    "price": row["price"],
                    "expiration_date": row["expiration_date"],
                }
            )

    return product_list


def get_sold_data(list_test=[], print_out_of_stock=False):
    with open("data/sold.csv", "r") as new_file:
        fieldnames = ["id", "bought_id", "sell_date", "price"]
        csv_reader = csv.DictReader(new_file, fieldnames=fieldnames)
        sold_product_id_list = list_test
        not_in_stock = False
        for row in csv_reader:
            if row["bought_id"] != "":
                if row["bought_id"] not in list_test:
                    sold_product_id_list.append(row["bought_id"])
            else:
                not_in_stock = True

        if not_in_stock and print_out_of_stock:
            print("product not in stock")
    return sold_product_id_list
