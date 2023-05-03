# Imports
import argparse
import csv
from datetime import date
from settings import *
from functions.csv_functions import *
from classes.Product import *
from rich import print
from rich.traceback import install

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
install()


def main():
    parser = argparse.ArgumentParser(description="print you input in the command line")
    parser.add_argument("text", metavar="text", type=str, help="enter your text")
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
    arg = parser.parse_args()

    text = arg.text
    product_name = arg.product_name
    price = arg.price
    expiration_date = arg.expiration_date

    match text:
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

        case _:
            print("you fucked up")


if __name__ == "__main__":
    main()
