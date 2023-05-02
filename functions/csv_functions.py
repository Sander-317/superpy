import csv


def write_to_file(
    action,
    product_name,
    price,
    expiration_date,
):
    to_add = {
        "action": action,
        "product_name": product_name,
        "price": price,
        "expiration_date": expiration_date,
    }

    with open("data/inventory.csv", "a", newline="") as new_file:
        fieldnames = ["action", "product_name", "price", "expiration_date"]
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        csv_writer.writerow(to_add)
