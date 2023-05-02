import csv


def write_to_file(product):
    to_add = {
        "product_name": product.name,
        "price": product.price,
        "expiration_date": product.expiration,
    }

    with open("data/inventory.csv", "a", newline="") as new_file:
        fieldnames = ["product_name", "price", "expiration_date"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writerow(to_add)
