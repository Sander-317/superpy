from functions.csv_functions import *


class Product:
    def __init__(self, id, name, price, expiration):
        self.id = id
        self.name = name
        self.price = price
        self.expiration = expiration

    def buy(self):
        write_to_file(self, "buy")

    def sell(self):
        write_to_file(self, "sell")