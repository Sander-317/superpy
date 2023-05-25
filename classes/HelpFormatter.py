import argparse


class CustomHelpFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super().__init__(prog, max_help_position=40, width=80)

    def _format_action_invocation(self, action):
        if not action.option_strings or action.nargs == 0:
            return super()._format_action_invocation(action)
        default = self._get_default_metavar_for_optional(action)
        args_string = self._format_args(action, default)
        return ", ".join(action.option_strings) + " " + args_string


# fmt = lambda prog: CustomHelpFormatter(prog)
# parser = argparse.ArgumentParser(formatter_class=fmt)

from typing import List


class SmartFormatter(argparse.HelpFormatter):
    def _split_lines(self, text: str, width: int) -> List[str]:
        lines: List[str] = []
        for line_str in text.split("\n"):
            line: List[str] = []
            line_len = 0
            for word in line_str.split():
                word_len = len(word)
                next_len = line_len + word_len
                if line:
                    next_len += 1
                if next_len > width:
                    lines.append(" ".join(line))
                    line.clear()
                    line_len = 0
                elif line:
                    line_len += 1

                line.append(word)
                line_len += word_len

            lines.append(" ".join(line))
        return lines

    def _fill_text(self, text: str, width: int, indent: str) -> str:
        return "\n".join(
            indent + line for line in self._split_lines(text, width - len(indent))
        )
