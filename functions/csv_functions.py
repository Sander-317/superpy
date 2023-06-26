import csv
from datetime import timedelta, date
from functions.functions import *
from rich.console import Console
from rich.traceback import install


install(show_locals=True)
console = Console()


def get_settings_data(action=""):
    import settings

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
        if action == "id":
            new_id = int(settings_list[0][action]) + 1
            settings.change_setting("id", str(new_id))
            return settings_list[0][action]

        else:
            return settings_list[0][action]

    else:
        return settings_list[0]


def write_settings_data(settings_dict):
    with open("data/settings.csv", "w") as setting_csv:
        fieldnames = ["color", "alignment", "today", "id"]
        csv_writer = csv.DictWriter(setting_csv, fieldnames=fieldnames)
        csv_writer.writerow(settings_dict)


text_color = get_settings_data("color")
text_align = get_settings_data("alignment")


def buy_product(
    product_name,
    price,
    expiration_date,
):
    with open("data/bought.csv", "a", newline="") as new_file:
        fieldnames = [
            "id",
            "buy_date",
            "product_name",
            "price",
            "expiration_date",
        ]
        to_add = {
            "id": get_settings_data("id"),
            "buy_date": get_settings_data("today"),
            "product_name": product_name,
            "price": price,
            "expiration_date": expiration_date,
        }
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writerow(to_add)
        create_report_data(
            "buy",
            to_add["buy_date"],
            to_add["price"],
        )


def sell_product(
    product_name,
    price,
    hide_print_out=False,
):
    from functions.csv_functions import text_color, text_align
    from settings import back_or_quit

    product_data = get_bought_data()
    product_list = get_product_list(product_data)
    unique_product_list = sorted(set(product_list))
    sold_products_id_list = get_sold_data()
    product_dict = get_dict_of_products(
        product_data, unique_product_list, sold_products_id_list
    )

    with open("data/sold.csv", "a", newline="") as new_file:
        fieldnames = [
            "id",
            "bought_id",
            "sell_date",
            "price",
        ]

        bought_id = get_bought_id(product_name, product_dict, sold_products_id_list)

        to_add = {
            "id": get_settings_data("id"),
            "bought_id": bought_id,
            "sell_date": get_settings_data("today"),
            "price": price,
        }

        if to_add["bought_id"] == None:
            console.print("OUT OF STOCK", style="red on yellow", justify="center")

            return
        else:
            if hide_print_out == False:
                console.print(
                    f"you have sold {product_name} for {round(float(price),2)}",
                    style=text_color,
                    justify=text_align,
                )
            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
            csv_writer.writerow(to_add)
            create_report_data(
                "sell",
                to_add["sell_date"],
                to_add["price"],
            )


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
        {
            "id": id,
            "date": date,
            "cost": round(float(cost), 2),
            "revenue": round(float(revenue), 2),
            "profit": round(float(new_profit), 2),
        }
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
            csv_writer.writerow(
                {
                    "id": row["id"],
                    "date": row["date"],
                    "cost": round(float(row["cost"]), 2),
                    "revenue": round(float(row["revenue"]), 2),
                    "profit": round(float(row["profit"]), 2),
                }
            )


def advance_time(days):
    import settings

    new_date = date.fromisoformat(get_settings_data("today")) + timedelta(
        days=int(days)
    )
    for i in range(int(days)):
        check_day = date.fromisoformat(get_settings_data("today")) + timedelta(
            days=int(i)
        )
        check_if_day_is_in_report(str(check_day))
        check_expiration_date()
    settings.change_setting("today", new_date)

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


def get_sold_data(list_test=[]):
    with open("data/sold.csv", "r") as new_file:
        fieldnames = ["id", "bought_id", "sell_date", "price"]
        csv_reader = csv.DictReader(new_file, fieldnames=fieldnames)
        sold_product_id_list = list_test

        for row in csv_reader:
            if row["bought_id"] != "":
                if row["bought_id"] not in list_test:
                    sold_product_id_list.append(row["bought_id"])
                continue
            continue
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
