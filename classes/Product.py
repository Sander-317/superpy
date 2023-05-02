from functions.csv_functions import *


class Product:
    def __init__(self, name, price, expiration):
        self.name = name
        self.price = price
        self.expiration = expiration

    def buy(self):
        write_to_file(self)
