from rich.console import Console
import sys
from datetime import datetime, timedelta, date
from rich.traceback import install
from functions import csv_functions as csv_functions

install()
console = Console()

quit_text = " q to quit"
go_back_text = "b to go back"
input_text = "enter your option"


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
    back_or_quit(user_input, "main")

    if user_input == "1":
        change_visual_settings()
    elif user_input == "2":
        change_date()
    elif user_input == "3":
        change_files()


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
    back_or_quit(user_input, "main")
    change_visuals(user_input)


def change_visuals(
    change_visuals_input,
):
    if change_visuals_input == "1":
        change_text_color()

    if change_visuals_input == "2":
        change_text_alignment()

    print(f"change visuals {quit_text}")

    user_input = input("enter your option")
    back_or_quit(user_input, "main")


def change_date():
    print(f"change date {quit_text}")
    user_input = input("enter your option")
    back_or_quit(user_input, "main")


def change_files():
    print(f"change files{quit_text}")
    user_input = input("enter your option")
    back_or_quit(user_input, "main")


def quit_settings(input):
    if input == "q":
        sys.exit()
    else:
        pass


def go_back(input, function):
    if function == "main" and input == "b":
        main_settings()
    elif function == "visual" and input == "b":
        change_visual_settings()


def back_or_quit(input, return_point):
    if input == "q":
        sys.exit()
    elif input == "b":
        if return_point == "main":
            main_settings()
        elif return_point == "visual":
            change_visual_settings()
    pass


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
    user_input_color = input("enter your option")
    back_or_quit(user_input_color, "visual")
    new_color = ""
    if user_input_color == "1":
        new_color = "blue"
    elif user_input_color == "2":
        new_color = "magenta"
    elif user_input_color == "3":
        new_color = "white"

    if new_color == "blue" or "magenta" or "white":
        print("user_input3", user_input_color)
        settings_dict = csv_functions.get_settings_data()
        settings_dict["color"] = new_color
        csv_functions.write_settings_data(settings_dict)
        print("setting data", settings_dict)

        print(new_color)
        go_back(user_input_color, "main")


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
    back_or_quit(user_input, "visual")
    new_alignment = ""
    if user_input == "1":
        new_alignment = "center"
    elif user_input == "2":
        new_alignment = "left"
    elif user_input == "3":
        new_alignment = "right"
    change_setting("alignment", new_alignment)


def change_date():
    from functions.csv_functions import text_color, text_align

    change_date_text = f"""
    enter new today in YYYY-MM-DD format
    WARNING when you do this all data wil be deleted WARNING
    enter {quit_text} {go_back_text}
    """
    console.print(f"{change_date_text}", style=text_color, justify=text_align)
    date_format = "%Y-%m-%d"

    user_input_date = input("enter your option")
    back_or_quit(user_input_date, "main")
    try:
        change_setting("date", datetime.strptime(user_input_date, date_format))
    except ValueError:
        console.print(
            "Incorrect date it should be YYYY-MM-DD",
            style="black on yellow",
            justify="center",
        )
        change_date()


def change_setting(setting, user_input):
    settings_dict = csv_functions.get_settings_data()
    settings_dict[setting] = user_input
    csv_functions.write_settings_data(settings_dict)
