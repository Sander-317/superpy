from rich.console import Console
from rich.text import Text
from rich.traceback import install

# from main import text_color, text_align

install()
console = Console()
text = Text()


text_color = "magenta"
text_align = "center"
quit_text = "enter q to quit"
input_text = "enter your option"


def settings():
    main_settings()


def main_settings():
    main_settings_text = f"""
welcome to setting what would you like to change 
                        
your current setting are text color: {text_color} and text align: {text_align} 
                        
1. change visuals 
2. option 
3. option 
{quit_text}
"""

    console.print(f"{main_settings_text}", style=text_color, justify=text_align)

    user_input = input("enter your option")

    quit_settings(user_input)
    if user_input == "1":
        change_visual_settings("1")


def change_visual_settings(user_input):
    if user_input == "1":
        console.print(
            "would you like to change the text color or alignment",
            style=text_color,
            justify=text_align,
        )
        console.print(
            "1. text color ",
            style=text_color,
            justify=text_align,
        )
        console.print(
            "1. text alignment",
            style=text_color,
            justify=text_align,
        )
        console.print(
            "1. both",
            style=text_color,
            justify=text_align,
        )
        user_input = input(
            "enter your option",
        )

        quit_settings(user_input)


def change_visuals():
    pass


def quit_settings(input):
    if input == "quit" or "q":
        return
