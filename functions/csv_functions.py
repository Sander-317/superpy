import csv


def write_to_file(product, action):
    match action:
        case "buy":
            to_add = {
                "product_name": product.name,
                "price": product.price,
                "expiration_date": product.expiration,
            }

            with open("data/bought.csv", "a", newline="") as new_file:
                fieldnames = ["product_name", "price", "expiration_date"]
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                csv_writer.writerow(to_add)
        case "sell":
            to_add = {
                "product_name": product.name,
                "price": product.price,
                "expiration_date": product.expiration,
            }

            with open("data/sold.csv", "a", newline="") as new_file:
                fieldnames = ["product_name", "price", "expiration_date"]
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                csv_writer.writerow(to_add)
        case _:
            print("write to file match statement")
