# report

---

## update:

i got the assignment back with the issue that you were able to sell stuff when its out of stock and you were able to enter wrong information

zo i fixed the sold out because a had it and broke it and i put try except in all the user input

and i added a simulate data feature in the settings its in settings under data please try it i am really proud of it

```python


products_list = [
    {"product_name": "apple", "price": 0.9, "expiration_date": ""},
    {"product_name": "banana", "price": 0.7, "expiration_date": ""},
    {"product_name": "melon", "price": 1, "expiration_date": ""},
    {"product_name": "kiwi", "price": 0.5, "expiration_date": ""},
    {"product_name": "dragon_fruit", "price": 1.5, "expiration_date": ""},
    {"product_name": "pineapple", "price": 0.95, "expiration_date": ""},
    {"product_name": "lemon", "price": 0.35, "expiration_date": ""},
]


def build_bought_file(
    number_of_days,
    max_products_per_day=10,
):
    for i in range(number_of_days):
        today = get_settings_data("today")
        check_if_day_is_in_report(today)
        for i in range(max_products_per_day):
            product = products_list[random.randint(0, len(products_list) - 1)]
            expiration_date = date.fromisoformat(
                get_settings_data("today")
            ) + timedelta(days=5)
            product["expiration_date"] = "{}-{}-{}".format(
                expiration_date.year, expiration_date.month, expiration_date.day
            )

            buy_product(
                product["product_name"], product["price"], product["expiration_date"]
            )
            if (i % 2) == 0:
                sell_product(product["product_name"], random.randint(1, 5), True)

        advance_time(1)

```

---

I think the module is to hard. You get so much new stuff at once its overwhelming. I started figuring out how argparse works. Slowly i started to understand more and more and finely i figured out what my plan was and tackled the problems one by one and i really like it in the end. I really wonder what you think and what i could have done better.

please check out:

```
python superpy.py settings
```

## i worked really hard on it

## problem one

the first big problem i encountered was the inventory table i wanted to show the inventory that was easy enough but then i thought of the fact that the a product can have multiple expiration dates zo i created the get_inventory_table() function.

```python
    def get_inventory_table(product_dict, average_price_dict, sold_products_id_list, today):
    from functions.csv_functions import text_color, text_align

    table = Table(title="inventory", box=box.MINIMAL_DOUBLE_HEAD)

    table.add_column("name", style=text_color, justify="center")
    table.add_column("count", style=text_color, justify="center")
    table.add_column("price", style="yellow", justify="center")
    table.add_column("expiration date", style=text_color, justify="center")

    for product in product_dict:
        expiration_dates = get_unique_expiration_dates(product_dict[product])
        for date in expiration_dates:
            product_list_by_day = []
            for product_in_dict in product_dict[product]:
                if datetime.strptime(
                    product_in_dict["expiration_date"], "%Y-%m-%d"
                ) >= datetime.strptime(today, "%Y-%m-%d") and datetime.strptime(
                    product_in_dict["buy_date"], "%Y-%m-%d"
                ) <= datetime.strptime(
                    today, "%Y-%m-%d"
                ):
                    if product_in_dict["id"] not in sold_products_id_list:
                        if product_in_dict["expiration_date"] == date:
                            product_list_by_day.append(product_in_dict)
                    else:
                        continue
                else:
                    sold_products_id_list.append(product_in_dict["id"])

                    continue
            if product_list_by_day != []:
                table.add_row(
                    product_list_by_day[0]["product_name"],
                    str(len(product_list_by_day)),
                    str(average_price_dict[product]),
                    date,
                )
    table = Align.center(table, vertical="middle")
    console = Console()
    console.print(table)

```

---

## problem two

I joined a live lesson about the walrus operator during the lesson i thought you can never use this. Zo i challenged my self to use it in the code in a way that make sense. I tried for a day or so then i gave up. Some days went by i suddenly i saw it in the get_id() and the get_today() functions and now they use a walrus operator.

```python
    def get_id():  # Walrus in function
    with open("data/id.csv", "r") as csv_id:
        csv_reader = csv.reader(csv_id)
        for row in csv_reader:
            (id := row[0])
    with open("data/id.csv", "w") as csv_id:
        csv_writer = csv.writer(csv_id)
        csv_writer.writerow(
            [
                int(id) + 1,
            ]
        )
    return id


def get_today():  # Walrus in function
    with open("data/today.csv", "r") as csv_id:
        csv_reader = csv.reader(csv_id)
        for row in csv_reader:
            (today := row[0])
    return today
```

but then the refactoring had begun and i killed walrus along with 2 other functions and turn it into something special the get settings data function (see be low)

```python
def get_settings_data(action=""):
    import settings

    with open("data/settings.csv", "r") as settings_file:
        fieldnames = ["color", "alignment", "today", "id"]
        csv_reader = csv.DictReader(settings_file, fieldnames=fieldnames)
        settings_list = []
        for row in csv_reader:
            settings_list.append(
                {
                    "color": row["color"],
                    "alignment": row["alignment"],
                    "today": row["today"],
                    "id": row["id"],
                }
            )
    if action != "":
        if action == "id":
            new_id = int(settings_list[0][action]) + 1
            settings.change_setting("id", str(new_id))
            return settings_list[0][action]

        else:
            return settings_list[0][action]

    else:
        return settings_list[0]


def write_settings_data(settings_dict):
    with open("data/settings.csv", "w") as setting_csv:
        fieldnames = ["color", "alignment", "today", "id"]
        csv_writer = csv.DictWriter(setting_csv, fieldnames=fieldnames)
        csv_writer.writerow(settings_dict)
```

## problem tree

I was gonna add the functionality to profit revenue table arguments. I thought i needed to make a lot of functions for the today yesterday and date arguments. But after some thinking i created get_report_specific_data() function to handle it all.

```python
    def get_report_specific_data(report_data, action_date, action):
    new_list = []
    for report in report_data:
        if str(action_date) in str(report["date"]):
            new_list.append(report)
    if action == "table":
        create_report_table(new_list)
    else:
        total_amount = round(sum(float(item[action]) for item in new_list), 2)
        if len(action_date) > 7:
            print(f"the {action} of {action_date} is  {total_amount}")
        else:
            new_action_date = action_date + "-01"
            new_date = date.fromisoformat(new_action_date)
            print(f"the {action} of {new_date.strftime('%B %Y')} is {total_amount}")

```

## Bonus Problem

In the function write_to_report_csv() i needed to sort a list of dicts by date and thats a nightmare to figure out. Zo what i did to fix it. I made a list of just the date because i went trough that nightmare already zo i sorted the list by date and then i looped over the list and made a new list of the dicts in the right order.

```python
    def write_to_report_csv(report_data):
    report_date_list = []
    for data in report_data:
        report_date_list.append(data["date"])
    sorted_report_data = []
    for date in sort_dates(report_date_list, True):
        for report in report_data:
            if report["date"] == date:
                sorted_report_data.append(report)
    with open(
        "data/report.csv",
        "w",
    ) as csv_report:
        fieldnames = ["id", "date", "cost", "revenue", "profit"]
        csv_writer = csv.DictWriter(csv_report, fieldnames=fieldnames)
        for row in sorted_report_data:
            csv_writer.writerow(row)
```
