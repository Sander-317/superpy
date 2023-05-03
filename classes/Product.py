from functions.csv_functions import *


class Buy_product:
    def __init__(self, id, name, price, expiration):
        self.id = id
        self.name = name
        self.price = price
        self.expiration = expiration

    def buy(self):
        write_to_file(self, "buy")


class Sell_product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sell(self):
        write_to_file(self, "sell")
