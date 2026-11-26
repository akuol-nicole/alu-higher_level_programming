#!/usr/bin/python3
"""Defines a text-indentation function.

Provides `text_indentation` which formats strings by adding two newlines
after `.`, `?`, and `:` characters while stripping leading and trailing spaces
on every printed line.
"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = ""
    for ch in text:
        if ch == "\n":
            print(buf.strip(" "))
            buf = ""
        elif ch in ".?:":
            buf += ch
            print(buf.strip(" "))
            print("")
            buf = ""
        else:
            buf += ch

    if buf:
        print(buf.strip(" "), end="")
