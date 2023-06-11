import csv
from datetime import datetime, timedelta, date
from functions.functions import *

from rich import print
from rich.console import Console
from rich.traceback import install

# from functions.settings import text_color, text_align
# import settings

# from functions.settings import text_color, text_align
install()
console = Console()


def get_settings_data(action=""):
    with open("data/settings.csv", "r") as settings_file:
        fieldnames = ["color", "alignment", "today", "id"]
        csv_reader = csv.DictReader(settings_file, fieldnames=fieldnames)
        settings_list = []
        for row in csv_reader:
            settings_list.append(
                {
                    "color": row["color"],
                    "alignment": row["alignment"],
                    "today": row["today"],
                    "id": row["id"],
                }
            )
    if action != "":
        return settings_list[0][action]
    else:
        return settings_list[0]


def write_settings_data(settings_dict):
    # print("WRITE SETTINGS", settings_dict)
    with open("data/settings.csv", "w") as setting_csv:
        fieldnames = ["color", "alignment", "today", "id"]
        csv_writer = csv.DictWriter(setting_csv, fieldnames=fieldnames)
        csv_writer.writerow(settings_dict)


# text_color = csv_functions.get_settings_data("color")
text_color = get_settings_data("color")
# text_align = csv_functions.get_settings_data("align")
text_align = get_settings_data("alignment")


def buy_product(product_name, price, expiration_date, report_data=""):
    report_data = get_report_data()
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
        create_report_data("buy", to_add["buy_date"], to_add["price"], report_data)


def sell_product(product_name, price, product_dict, sold_products_id_list, report_data):
    with open("data/sold.csv", "a", newline="") as new_file:
        fieldnames = [
            "id",
            "bought_id",
            "sell_date",
            "price",
        ]
        to_add = {
            "id": get_id(),
            "bought_id": get_bought_id(
                product_name, product_dict, sold_products_id_list
            ),
            "sell_date": get_today(),
            "price": price,
        }
        # print(to_add["bought_id"])
        if to_add["bought_id"] == None:
            console.print("OUT OF STOCK", style="red on yellow", justify="center")

            return
        else:
            console.print(
                f"you have sold {product_name} for {round(float(price),2)}",
                style=settings.text_color,
                justify=settings.text_align,
            )
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writerow(to_add)
            create_report_data(
                "sell", to_add["sell_date"], to_add["price"], report_data
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
    return new_list


def add_report_data(
    id,
    date,
    cost,
    revenue,
):
    report_data = get_report_data()
    new_profit = revenue - cost
    report_data.append(
        {"id": id, "date": date, "cost": cost, "revenue": revenue, "profit": new_profit}
    )
    write_to_report_csv(report_data)


def write_to_report_csv(report_data):
    report_date_list = []
    for data in report_data:
        report_date_list.append(data["date"])
    sorted_report_data = []
    for date in sort_dates(report_date_list, True):
        for report in report_data:
            if report["date"] == date:
                sorted_report_data.append(report)
    with open(
        "data/report.csv",
        "w",
    ) as csv_report:
        fieldnames = ["id", "date", "cost", "revenue", "profit"]
        csv_writer = csv.DictWriter(csv_report, fieldnames=fieldnames)
        for row in sorted_report_data:
            csv_writer.writerow(row)


def advance_time(days):
    new_date = date.fromisoformat(get_today()) + timedelta(days=int(days))
    for i in range(int(days)):
        check_day = date.fromisoformat(get_today()) + timedelta(days=int(i))
        check_if_day_is_in_report(str(check_day))
    change_today(new_date)
    return new_date


def change_today(new_today):
    new_list = []
    new_list.append(new_today)
    with open("data/today.csv", "w") as csv_today:
        csv_writer = csv.writer(csv_today)
        csv_writer.writerow(new_list)
        new_list = []


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


def clear_files():
    import settings

    files = ["data/sold.csv", "data/bought.csv", "data/report.csv"]
    empty = ""
    for file in files:
        with open(file, "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(empty)
    settings.change_setting("id", "0")
