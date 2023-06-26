# Imports
import argparse
from functions.csv_functions import *
from functions.functions import *
from create_test_data.create_bought_file_data import *
from classes.HelpFormatter import *
from rich.traceback import install
from rich.console import Console
import settings


# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.

install(show_locals=True)
console = Console()


def main():
    from functions.csv_functions import text_color, text_align

    today = get_settings_data("today")
    product_data = get_bought_data()
    product_list = get_product_list(product_data)
    unique_product_list = sorted(set(product_list))
    report_data = get_report_data()
    test = get_sold_data()
    sold_products_id_list = get_sold_data(test)
    product_dict = get_dict_of_products(
        product_data, unique_product_list, sold_products_id_list
    )
    average_price_dict = get_average_price_dict(product_dict)

    fmt = lambda prog: CustomHelpFormatter(prog)

    parser = argparse.ArgumentParser(
        description=" welcome to Super py", formatter_class=fmt
    )

    parser.add_argument(
        "action1",
        metavar="action 1",
        type=str,
        nargs="?",
        help="enter your action options are [buy, sell, report, settings]",
    )
    parser.add_argument(
        "action2",
        metavar="action 2",
        type=str,
        default="5",
        nargs="?",
        help="if first action is report the options are [inventory, revenue, profit, table] ",
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
        "-ed",
        "--expiration_date",
        action="store",
        help="enter the expiration date YYYY-MM-DD",
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
        help="gets value of yesterday can be used for report [inventory, profit, revenue]",
    )
    parser.add_argument(
        "-td",
        "--today",
        action="store_true",
        help="gets value of yesterday can be used for report [inventory, profit, revenue]",
    )

    parser.add_argument(
        "-d",
        "--date",
        action="store",
        help="gets value of specific date can be used for report [inventory, profit, revenue]",
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
    yesterday_arg = arg.yesterday
    today_arg = arg.today
    date_arg = arg.date
    advance_number_of_days = arg.advance_time

    match action_one:
        case None:
            try:
                int(advance_number_of_days)
                advance_time(advance_number_of_days)
                console.print(
                    "you have advanced to ",
                    date.fromisoformat(get_settings_data("today")),
                    style=text_color,
                    justify=text_align,
                )
            except Exception:
                console.print(
                    "make sure you enter a number ",
                    style=text_color,
                    justify=text_align,
                )

        case "buy":
            try:
                datetime.strptime(expiration_date, "%Y-%m-%d")
                float(price)
                if len(product_name) == 0:
                    raise Exception
                buy_product(
                    product_name,
                    price,
                    expiration_date,
                )
                console.print(
                    f"you have added 1 {product_name} you bought for {round(float(price),2)} and expires on {expiration_date}",
                    style="blue",
                    justify="center",
                )
            except Exception:
                console.print(
                    "make sure you enter a product name and enter a number for the price and a valid date 'YYYY-MM-DD' ",
                    style=text_color,
                    justify=text_align,
                )

        case "sell":
            try:
                float(price)
                if len(product_name) == 0:
                    raise Exception
                if product_name not in unique_product_list:
                    raise Exception
                sell_product(
                    product_name,
                    price,
                )
            except:
                console.print(
                    "make sure you enter a valid product name (check inventory) and enter a number for the price",
                    style=text_color,
                    justify=text_align,
                )

        case "settings":
            settings.main_settings()

        case "report":
            if action_two == "inventory":
                if yesterday_arg:
                    get_inventory_table(
                        product_dict,
                        average_price_dict,
                        sold_products_id_list,
                        get_yesterday(),
                    )

                elif today_arg:
                    get_inventory_table(
                        product_dict,
                        average_price_dict,
                        sold_products_id_list,
                        today,
                    )

                elif date_arg:
                    get_inventory_table(
                        product_dict,
                        average_price_dict,
                        sold_products_id_list,
                        date_arg,
                    )

            elif action_two == "revenue":
                if yesterday_arg:
                    get_report_specific_data(report_data, get_yesterday(), "revenue")

                elif today_arg:
                    get_report_specific_data(report_data, today, "revenue")

                elif date_arg:
                    get_report_specific_data(report_data, date_arg, "revenue")

            elif action_two == "profit":
                if yesterday_arg:
                    get_report_specific_data(report_data, get_yesterday(), "profit")

                elif today_arg:
                    get_report_specific_data(report_data, today, "profit")

                elif date_arg:
                    get_report_specific_data(report_data, date_arg, "profit")

            elif action_two == "table":
                if yesterday_arg:
                    get_report_specific_data(report_data, get_yesterday(), "table")

                elif today_arg:
                    get_report_specific_data(report_data, today, "table")

                elif date_arg:
                    get_report_specific_data(report_data, date_arg, "table")
                else:
                    create_report_table(report_data)

        case _:
            pass


if __name__ == "__main__":
    console.print(
        "today is",
        date.fromisoformat(get_settings_data("today")),
        style=text_color,
        justify=text_align,
    )
    check_if_day_is_in_report(get_settings_data("today"))
    check_expiration_date()
    main()
