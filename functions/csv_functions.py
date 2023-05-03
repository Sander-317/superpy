import csv
from rich.table import Table
from rich.console import Console


def write_to_file(product, action):
    match action:
        case "buy":
            to_add = {
                "id": product.id,
                "product_name": product.name,
                "price": product.price,
                "expiration_date": product.expiration,
            }

            with open("data/bought.csv", "a", newline="") as new_file:
                fieldnames = ["id", "product_name", "price", "expiration_date"]
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                csv_writer.writerow(to_add)
        case "sell":
            to_add = {
                "product_name": product.name,
                "price": product.price,
            }

            with open("data/sold.csv", "a", newline="") as new_file:
                fieldnames = [
                    "product_name",
                    "price",
                ]
                csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                csv_writer.writerow(to_add)
        case _:
            print("write to file match statement")


def get_id():
    find_id = []
    with open("data/id.csv", "r") as csv_id:
        csv_reader = csv.reader(csv_id)
        for row in csv_reader:
            find_id.append(row[0])

    print("id", find_id[0])
    with open("data/id.csv", "w") as csv_id:
        csv_writer = csv.writer(csv_id)
        csv_writer.writerow(
            [
                int(find_id[0]) + 1,
            ]
        )
    return find_id[0]


def get_inventory():
    table = Table(title="inventory")
    table.add_column("name")
    table.add_column("count")
    table.add_column("price")
    table.add_column("expiration date")
    with open("data/bought.csv", "r") as new_file:
        fieldnames = ["id", "product_name", "price", "expiration_date"]
        csv_reader = csv.DictReader(new_file, fieldnames=fieldnames)
        product_list = []
        for i in csv_reader:
            product_list.append(i["product_name"])
            # print(i)
            table.add_row(i["product_name"], "1", i["price"], i["expiration_date"])
        unique_product_list = set(product_list)
        print(unique_product_list)
    console = Console()
    console.print(table)
