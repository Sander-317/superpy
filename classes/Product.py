from functions.csv_functions import *


class Buy_product:
    def __init__(self, id, name, price, expiration):
        self.id = id
        self.buy_date = ""
        self.name = name
        self.price = price
        self.expiration = expiration

    def buy(self):
        write_to_file(self, "buy")


# TODO: (id,bought_id,sell_date,sell_price)
class Sell_product:
    def __init__(self, name, price):
        # self.id = id

        self.name = name
        self.price = price

    def sell(self):
        print("self in sell: ", self)
        write_to_file(self, "sell")
