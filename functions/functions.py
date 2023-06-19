from . import csv_functions as csv_functions
from datetime import datetime, timedelta, date
from rich.table import Table
from rich.console import Console
from rich.align import Align
from rich import box
import settings
from re import search


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


def get_inventory_table(product_dict, average_price_dict, sold_products_id_list, today):
    from functions.csv_functions import text_color, text_align

    table = Table(title="inventory", box=box.MINIMAL_DOUBLE_HEAD)

    table.add_column("name", style=text_color, justify="center")
    table.add_column("count", style=text_color, justify="center")
    table.add_column("price", style="yellow", justify="center")
    table.add_column("expiration date", style=text_color, justify="center")

    for product in product_dict:
        expiration_dates = get_unique_expiration_dates(product_dict[product])
        for date in expiration_dates:
            product_list_by_day = []
            for product_in_dict in product_dict[product]:
                if datetime.strptime(
                    product_in_dict["expiration_date"], "%Y-%m-%d"
                ) >= datetime.strptime(today, "%Y-%m-%d") and datetime.strptime(
                    product_in_dict["buy_date"], "%Y-%m-%d"
                ) <= datetime.strptime(
                    today, "%Y-%m-%d"
                ):
                    if product_in_dict["id"] not in sold_products_id_list:
                        if product_in_dict["expiration_date"] == date:
                            product_list_by_day.append(product_in_dict)
                    else:
                        continue
                else:
                    sold_products_id_list.append(product_in_dict["id"])

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
            else:
                return None
    else:
        return None


def get_report_dates(report_data):
    new_list = []
    for date in report_data:
        new_list.append(date["date"])
    return new_list


def create_report_data(action, buy_date, buy_price, report_data):
    print(report_data)
    for date in report_data:
        if date["date"] == buy_date:
            if action == "buy":
                date.update({"cost": str(float(date["cost"]) + float(buy_price))})

                date.update(
                    {"profit": str(float(date["revenue"]) - float(date["cost"]))}
                )
                break
            elif action == "sell":
                date.update({"revenue": str(float(date["revenue"]) + float(buy_price))})
                date.update(
                    {"profit": str(float(date["revenue"]) - float(date["cost"]))}
                )
                print(report_data)
                break

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


def get_report_specific_data(report_data, action_date, action):
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
                style=settings.text_color,
                justify=settings.text_align,
            )
        else:
            new_action_date = action_date + "-01"
            new_date = date.fromisoformat(new_action_date)
            console.print(
                f"the {action} of {new_date.strftime('%B %Y')} is {total_amount}",
                style=settings.text_color,
                justify=settings.text_align,
            )


def get_yesterday():
    yesterday = date.fromisoformat(csv_functions.get_today()) - timedelta(days=int(1))
    return yesterday
