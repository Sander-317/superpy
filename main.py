# Imports
import argparse
import csv
from datetime import date
from functions.csv_functions import *
from classes.Product import *
from rich import print

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
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
    # write_to_file(text, product_name, price, expiration_date)
    Product(product_name, price, expiration_date).buy()
    Product(product_name, price, expiration_date).sell()
    print(
        f"text = {text} product_name = {product_name} price = {price} expiration date = {expiration_date}"
    )


if __name__ == "__main__":
    main()
