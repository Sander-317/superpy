# Imports
import argparse
import csv

# from datetime import date
# import datetime
from functions.csv_functions import *
from functions.functions import *
from create_test_data.create_bought_file_data import *

from classes.HelpFormatter import *
from rich import print
from rich.traceback import install

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
install()


def main():
    today = get_today()
    product_data = get_bought_data()
    product_list = get_product_list(product_data)
    unique_product_list = sorted(set(product_list))
    report_data = get_report_data()
    # print("report data:", report_data)
    report_data_dates = get_report_dates(report_data)
    # print(report_data_dates)
    # check_if_day_is_in_report(report_data_dates)
    test = get_sold_data()
    sold_products_id_list = get_sold_data(test, True)

    product_dict = get_dict_of_products(
        product_data, unique_product_list, sold_products_id_list
    )
    average_price_dict = get_average_price_dict(product_dict)
    print("sold products id list main.py", sold_products_id_list)

    fmt = lambda prog: CustomHelpFormatter(prog)

    parser = argparse.ArgumentParser(formatter_class=fmt)
    # parser = argparse.ArgumentParser(formatter_class=SmartFormatter)
    # parser = argparse.ArgumentParser(description="Super py")
    parser.add_argument(
        "action1",
        metavar="action 1",
        type=str,
        nargs="?",
        help="enter your action options are [buy, sell, report]",
    )
    parser.add_argument(
        "action2",
        metavar="action 2",
        type=str,
        default="5",
        nargs="?",
        help="if first action is report the options are [inventory, revenue, profit] ",
    )
    parser.add_argument(
        "-pn",
        "--product_name",
        action="store",
        help="enter the name of the product",
    )
    parser.add_argument(
        "-p", "--price", action="store", help="enter the price of the product"
    )
    parser.add_argument(
        "-ed", "--expiration_date", action="store", help="enter the expiration date"
    )
    parser.add_argument(
        "-n",
        "--now",
        action="store_true",
        help="gets inventory now first action needs to be report action 2 needs to be inventory",
    )
    parser.add_argument(
        "-yd",
        "--yesterday",
        action="store_true",
        help="gets value of yesterday",
    )
    parser.add_argument(
        "-td",
        "--today",
        action="store_true",
        help="gets value of yesterday",
    )

    parser.add_argument(
        "-d",
        "--date",
        action="store",
        help="gets value of specific date",
    )
    parser.add_argument(
        "-at",
        "--advance_time",
        action="store",
        help="advances time by the number provided",
    )

    arg = parser.parse_args()

    action_one = arg.action1
    action_two = arg.action2
    product_name = arg.product_name
    price = arg.price
    expiration_date = arg.expiration_date
    now = arg.now
    yesterday_arg = arg.yesterday
    today_arg = arg.today
    date_arg = arg.date
    advance_number_of_days = arg.advance_time

    # today = get_today()
    # product_data = get_bought_data()
    # product_list = get_product_list(product_data)
    # unique_product_list = sorted(set(product_list))
    # report_data = get_report_data()
    # # print("report data:", report_data)
    # report_data_dates = get_report_dates(report_data)
    # # print(report_data_dates)
    # check_if_day_is_in_report(report_data_dates)
    # test = get_sold_data()
    # sold_products_id_list = get_sold_data(test, True)

    # product_dict = get_dict_of_products(
    #     product_data, unique_product_list, sold_products_id_list
    # )
    # average_price_dict = get_average_price_dict(product_dict)
    # print("sold products id list main.py", sold_products_id_list)

    match action_one:
        case None:
            advance_time(advance_number_of_days)
            print("new today", date.fromisoformat(get_today()))
        case "buy":
            buy_product(product_name, price, expiration_date, report_data)
            print(
                f"you have added 1 {product_name} you bought for {price} and expires on {expiration_date}"
            )
        case "sell":
            sell_product(
                product_name, price, product_dict, sold_products_id_list, report_data
            )
            # print(f"you have sold {product_name} for {price}")

        case "report":
            if action_two == "inventory":
                if now == True:
                    # print("yeeey inventory now")
                    get_inventory_table(
                        product_dict, average_price_dict, sold_products_id_list, today
                    )
                else:
                    print("yeeey inventory")
            elif action_two == "revenue":
                if yesterday_arg:
                    yesterday = get_yesterday()
                    get_report_specific_data(report_data, yesterday)
                    print("revenue yesterday")
                elif today_arg:
                    get_report_specific_data(report_data, get_today())
                    print("revenue today")
                elif date_arg:
                    get_report_specific_data(report_data, date_arg)
                    print(f"revenue date: {date_arg}")
            elif action_two == "profit":
                print("yeeey profit")
            elif action_two == "all":
                create_report_table(report_data)

        case _:
            pass
            # print("you fucked up")


if __name__ == "__main__":
    print("today main.py", date.fromisoformat(get_today()))
    # check_if_day_is_in_report(date.fromisoformat(get_today()))
    check_if_day_is_in_report(get_today())
    # get_today()
    # build_bought_file(10, 10)
    main()
