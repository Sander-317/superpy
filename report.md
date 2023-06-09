# report

I think the module is to hard. You get so much new stuff at once its overwhelming. I started figuring out how argparse works. Slowly i started to understand more and more and finely i figured out what my plan was and tackled the problems one by one and i really like it in the end. I really wonder what you think and what i could have done better.

---

## problem one

the first big problem i encountered was the inventory table i wanted to show the inventory that was easy enough but then i thought of the fact that the a product can have multiple expiration dates zo i created the get_inventory_table() function.

```python
    def get_inventory_table(product_dict, average_price_dict, sold_products_id_list, today):
    table = Table(title="inventory")
    table.add_column("name")
    table.add_column("count")
    table.add_column("price")
    table.add_column("expiration date")

    for product in product_dict:
        expiration_dates = get_unique_expiration_dates(product_dict[product])
        for date in expiration_dates:
            product_list_by_day = []
            for product_in_dict in product_dict[product]:
                if datetime.strptime(
                    product_in_dict["expiration_date"], "%Y-%m-%d"
                ) >= datetime.strptime(today, "%Y-%m-%d"):
                    if product_in_dict["id"] not in sold_products_id_list:
                        if product_in_dict["expiration_date"] == date:
                            product_list_by_day.append(product_in_dict)
                    else:
                        continue
                else:
                    continue
            if product_list_by_day != []:
                table.add_row(
                    product_list_by_day[0]["product_name"],
                    str(len(product_list_by_day)),
                    str(average_price_dict[product]),
                    date,
                )

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
