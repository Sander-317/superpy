# Imports
import argparse
import csv
from datetime import date
from settings import *
from functions.csv_functions import *
from functions.functions import *
from classes.Product import *
from rich import print
from rich.traceback import install

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
install()


def main():
    parser = argparse.ArgumentParser(description="Super py")
    parser.add_argument(
        "action1",
        metavar="action 1",
        type=str,
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
    parser.add_argument("-n", "--now", action="store_true", help="gets inventory now")

    arg = parser.parse_args()

    action_one = arg.action1
    action_two = arg.action2
    product_name = arg.product_name
    price = arg.price
    expiration_date = arg.expiration_date
    now = arg.now

    match action_one:
        case "buy":
            Buy_product(get_id(), product_name, price, expiration_date).buy()
            print(
                f"you have added 1 {product_name} you bought for {price} and expires on {expiration_date}"
            )
        case "sell":
            Sell_product(
                product_name,
                price,
            ).sell()
        case "report":
            if action_two == "inventory":
                if now == True:
                    print("yeeey inventory now")
                    get_inventory()
                else:
                    print("yeeey inventory")
            elif action_two == "revenue":
                print("yeeey revenue")
            elif action_two == "profit":
                print("yeeey profit")

        case _:
            print("you fucked up")


if __name__ == "__main__":
    date.fromisoformat(get_today())
    get_today()
    main()
