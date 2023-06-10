from rich.console import Console
from rich.text import Text
from rich.traceback import install

# from main import text_color, text_align

install()
console = Console()
text = Text()


text_color = "magenta"
text_align = "center"
quit_text = " q to quit"
go_back_text = "b to go back"
input_text = "enter your option"


def settings():
    main_settings()


main_settings_text = f"""
welcome to setting what would you like to change 
                        
your current setting are text color: {text_color} and text align: {text_align} 
                        
1. change visuals 
2. change date 
3. change files
{quit_text}
"""


def main_settings():
    console.print(f"{main_settings_text}", style=text_color, justify=text_align)

    user_input = input(input_text)

    quit_settings(user_input)
    if user_input == "1":
        change_visual_settings()
    elif user_input == "2":
        change_date()
    elif user_input == "3":
        change_files()


change_visual_text = f"""
would you like to change the text color or alignment
1. text color 
2. text alignment
3. both
enter {quit_text} {go_back_text}
"""


def change_visual_settings():
    # if user_input == "1":
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
        pass
    if change_visuals_input == "3":
        pass
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


change_color_text = f"""
what text color would you like the current color is {text_color} the options are
1. blue
2. magenta
3. white
enter {quit_text} {go_back_text}
"""


def change_text_color():
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
        # global text_color
        # new_color = user_input3
        # text_color = new_color
        print(new_color)
        go_back(user_input3, "main")

    quit_settings(user_input3)
    go_back(user_input3, "visual")
