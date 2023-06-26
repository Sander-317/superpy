from . import csv_functions as csv_functions
from datetime import datetime, timedelta, date
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich import box


console = Console()


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


def sort_dates(dates, reverse=False):
    def date_key(date_string):
        return datetime.strptime(date_string, "%Y-%m-%d")

    if reverse:
        return sorted(dates, key=date_key, reverse=True)
    else:
        return sorted(
            dates,
            key=date_key,
        )


def get_inventory_table(
    product_dict, average_price_dict, sold_products_id_list, check_date
):
    from functions.csv_functions import text_color, text_align

    console = Console()

    table = Table(title="inventory", box=box.MINIMAL_DOUBLE_HEAD)

    table.add_column("name", style=text_color, justify="center")
    table.add_column("count", style=text_color, justify="center")
    table.add_column("price", style="yellow", justify="center")
    table.add_column("expiration date", style=text_color, justify="center")
    format = "%Y-%m-%d"
    try:
        datetime.strptime(check_date, format)
    except:
        console.print(
            "please enter valid dat format YYYY-MM-DD",
            style=text_color,
            justify="center",
        )
        return

    for product in product_dict:
        expiration_dates = get_unique_expiration_dates(product_dict[product])
        for date in expiration_dates:
            product_list_by_day = []
            for product_in_dict in product_dict[product]:
                if datetime.strptime(
                    product_in_dict["buy_date"], format
                ) <= datetime.strptime(check_date, format):
                    if product_in_dict["id"] not in sold_products_id_list:
                        if product_in_dict["expiration_date"] == date:
                            product_list_by_day.append(product_in_dict)
                    else:
                        continue

                    continue
            if product_list_by_day != []:
                table.add_row(
                    product_list_by_day[0]["product_name"],
                    str(len(product_list_by_day)),
                    str(average_price_dict[product]),
                    date,
                )
    table = Align.center(table, vertical="middle")
    console = Console()
    console.print(table)


def get_bought_id(product_name, product_dict, sold_products_id_list):
    if product_name in product_dict.keys():
        for product in product_dict[product_name]:
            if product["id"] != "":
                if product["id"] not in sold_products_id_list:
                    return product["id"]
                else:
                    return None


def get_report_dates(report_data):
    new_list = []
    for date in report_data:
        new_list.append(date["date"])
    return new_list


def create_report_data(
    action,
    date,
    buy_price,
):
    from functions.csv_functions import get_report_data

    report_data = get_report_data()

    for report_date in report_data:
        if report_date["date"] == date:
            if action == "buy":
                report_date.update(
                    {"cost": str(float(report_date["cost"]) + float(buy_price))}
                )

                report_date.update(
                    {
                        "profit": str(
                            float(report_date["revenue"]) - float(report_date["cost"])
                        )
                    }
                )

            elif action == "sell":
                report_date.update(
                    {"revenue": str(float(report_date["revenue"]) + float(buy_price))}
                )
                report_date.update(
                    {
                        "profit": str(
                            float(report_date["revenue"]) - float(report_date["cost"])
                        )
                    }
                )

    csv_functions.write_to_report_csv(report_data)


def create_report_table(report_data):
    from functions.csv_functions import text_color, text_align

    table = Table(title="report", box=box.MINIMAL_DOUBLE_HEAD)
    table.add_column("date", style=text_color, justify="center")
    table.add_column("cost", style="red", justify="center")
    table.add_column("revenue", style="green", justify="center")
    table.add_column("profit", style="yellow", justify="center")

    for data in report_data:
        table.add_row(
            data["date"],
            str(round(float(data["cost"]), 2)),
            str(round(float(data["revenue"]), 2)),
            str(round(float(data["profit"]), 2)),
        )
    table = Align.center(table, vertical="middle")
    console = Console()
    console.print(table)


def check_if_day_is_in_report(today):
    report_data = csv_functions.get_report_data()
    report_data_dates = csv_functions.get_report_dates(report_data)

    if today not in report_data_dates:
        csv_functions.add_report_data(
            csv_functions.get_settings_data("id"),
            today,
            0,
            0,
        )
    else:
        return


def get_report_specific_data(report_data, action_date, action):
    from functions.csv_functions import text_color, text_align

    new_list = []
    for report in report_data:
        if str(action_date) in str(report["date"]):
            new_list.append(report)
    if action == "table":
        create_report_table(new_list)
    else:
        total_amount = round(sum(float(item[action]) for item in new_list), 2)
        if len(str(action_date)) > 7:
            console.print(
                f"the {action} of {action_date} is {total_amount}",
                style=text_color,
                justify=text_align,
            )
        else:
            new_action_date = action_date + "-01"
            new_date = date.fromisoformat(new_action_date)
            console.print(
                f"the {action} of {new_date.strftime('%B %Y')} is {total_amount}",
                style=text_color,
                justify=text_align,
            )


def get_yesterday():
    yesterday = date.fromisoformat(
        csv_functions.get_settings_data("today")
    ) - timedelta(days=int(1))
    return yesterday


def check_expiration_date():
    from functions.csv_functions import (
        get_bought_data,
        get_settings_data,
        sell_product,
        get_sold_data,
    )

    today = get_settings_data("today")
    bought_data = get_bought_data()
    sold_ids = get_sold_data()
    for product in bought_data:
        if product["id"] not in sold_ids:
            if datetime.strptime(
                product["expiration_date"], "%Y-%m-%d"
            ) < datetime.strptime(today, "%Y-%m-%d"):
                sell_product(
                    product["product_name"],
                    0,
                    True,
                )
