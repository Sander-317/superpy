from rich.console import Console
import csv
from datetime import datetime, timedelta, date
from rich.traceback import install

install()

# from functions.csv_functions import *

# from . import csv_functions as csv_functions
# import csv_functions

from functions import csv_functions as csv_functions

# from main import text_color, text_align

# from main import text_color, text_align
# from functions.settings import text_color, text_align
# from functions.csv_functions import text_color, text_align

console = Console()


# def get_settings_data(action):
#     with open("../data/settings.csv", "r") as settings_file:
#         fieldnames = ["color", "align"]
#         csv_reader = csv.DictReader(settings_file, fieldnames=fieldnames)
#         settings_list = []
#         for row in csv_reader:
#             settings_list.append({"color": row["color"], "align": row["align"]})

#     print(settings_list[0]["color"])
#     return settings_list[0][action]

#     # with open("data/id.csv", "w") as csv_id:
#     #     csv_writer = csv.writer(csv_id)
#     #     csv_writer.writerow(
#     #         [
#     #             int(id) + 1,
#     #         ]
#     #     )
#     # return id


# text_color = get_settings_data("color")
# text_color = "magenta"
# text_color = csv_functions.get_settings_data("color")
# text_align = get_settings_data("align")
# text_align = "center"
quit_text = " q to quit"
go_back_text = "b to go back"
input_text = "enter your option"
# text_color = csv_functions.get_settings_data("color")
# text_align = csv_functions.get_settings_data("align")
# from main import text_color, text_align


def settings():
    # csv_functions.get_settings_data()
    # get_settings_data()
    main_settings()


# main_settings_text = f"""
# welcome to setting what would you like to change

# your current setting are text color: {text_color} and text align: {text_align}

# 1. change visuals
# 2. change date
# 3. change files
# {quit_text}
# """


def main_settings():
    from functions.csv_functions import text_color, text_align

    main_settings_text = f"""
welcome to setting what would you like to change 
                        
your current setting are text color: {text_color} and text align: {text_align} 
                        
1. change visuals 
2. change today 
3. clear files
{quit_text}
"""
    console.print(f"{main_settings_text}", style=text_color, justify=text_align)

    user_input = input(input_text)

    quit_settings(user_input)
    if user_input == "1":
        change_visual_settings()
    elif user_input == "2":
        change_date()
    elif user_input == "3":
        change_files()


# change_visual_text = f"""
# would you like to change the text color or alignment
# 1. text color
# 2. text alignment
# 3. both
# enter {quit_text} {go_back_text}
# """


def change_visual_settings():
    from functions.csv_functions import text_color, text_align

    change_visual_text = f"""
would you like to change the text color or alignment
1. text color
2. text alignment
enter {quit_text} {go_back_text}
"""

    console.print(f"{change_visual_text}", style=text_color, justify=text_align)

    user_input = input(input_text)
    go_back(user_input, "main")
    quit_settings(user_input)
    change_visuals(user_input)


def change_visuals(
    change_visuals_input,
):
    if change_visuals_input == "1":
        change_text_color()

    if change_visuals_input == "2":
        change_text_alignment()

    print(f"change visuals {quit_text}")

    user_input2 = input("enter your option")

    go_back(
        user_input2,
        "main",
    )
    quit_settings(user_input2)


def change_date():
    print(f"change date {quit_text}")
    user_input = input("enter your option")

    quit_settings(user_input)
    go_back(user_input, "main")


def change_files():
    print(f"change files{quit_text}")
    user_input = input("enter your option")

    quit_settings(user_input)
    go_back(user_input, "main")


def quit_settings(input):
    if input == "quit" or "q":
        return
    else:
        pass


def go_back(input, function):
    if function == "main" and input == "b":
        main_settings()
    elif function == "visual" and input == "b":
        change_visual_settings()


def change_text_color():
    from functions.csv_functions import text_color, text_align

    change_color_text = f"""
what text color would you like the current color is {text_color} the options are
1. blue
2. magenta
3. white
enter {quit_text} {go_back_text}
"""
    console.print(f"{change_color_text}", style=text_color, justify=text_align)
    user_input3 = input("enter your option")
    new_color = ""
    if user_input3 == "1":
        new_color = "blue"
    elif user_input3 == "2":
        new_color = "magenta"
    elif user_input3 == "3":
        new_color = "white"

    if new_color == "blue" or "magenta" or "white":
        print("user_input3", user_input3)
        settings_dict = csv_functions.get_settings_data()
        settings_dict["color"] = new_color
        csv_functions.write_settings_data(settings_dict)
        print("setting data", settings_dict)

        print(new_color)
        go_back(user_input3, "main")

    quit_settings(user_input3)
    go_back(user_input3, "visual")


def change_text_alignment():
    from functions.csv_functions import text_color, text_align

    change_text_alignment_text = f"""
what would you text alignment do you like to change?
1. center
2. left
3. right
enter {quit_text} {go_back_text}
"""
    console.print(f"{change_text_alignment_text}", style=text_color, justify=text_align)
    user_input = input("enter your option")
    new_alignment = ""
    if user_input == "1":
        new_alignment = "center"
    elif user_input == "2":
        new_alignment = "left"
    elif user_input == "3":
        new_alignment = "right"

    if new_alignment == "center" or "left" or "right":
        print("user_input3", user_input)
        settings_dict = csv_functions.get_settings_data()
        settings_dict["alignment"] = new_alignment
        csv_functions.write_settings_data(settings_dict)
        print("setting data", settings_dict)

        print(new_alignment)
        go_back(user_input, "main")

    quit_settings(user_input)
    go_back(user_input, "visual")


def change_date():
    from functions.csv_functions import text_color, text_align

    change_date_text = f"""
    enter new today in YYYY-MM-DD format
    WARNING when you do this all data wil be deleted WARNING
    """
    console.print(f"{change_date_text}", style=text_color, justify=text_align)
    date_format = "%Y-%m-%d"
    try:
        user_input = input("enter your option")
        dateObject = datetime.strptime(user_input, date_format)
        print(dateObject)
        settings_dict = csv_functions.get_settings_data()
        settings_dict["today"] = user_input
        csv_functions.write_settings_data(settings_dict)
        print("setting data", settings_dict)
        quit_settings(user_input)
        go_back(user_input, "main")

    except ValueError:
        console.print(
            "Incorrect date it should be YYYY-MM-DD",
            style="red on yellow",
            justify="center",
        )
        change_date()

    print(user_input)
    go_back(user_input, "main")
