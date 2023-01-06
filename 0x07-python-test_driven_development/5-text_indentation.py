#!/usr/bin/python3
"""
The `5-text_indentation` module
"""

def text_indentation(text):
    """Function that prints a text with 2 new lines
        after each of these characters: `.`, `?`, `:`
    Args:
        text (str): text variable to hold string
    Returns:
        a text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if (text[i] == "." or text[i] == "?" or text[i] == ":"):
            text = text.replace("{} ".format(text[i]), "{}\n\n".format(text[i]))
        i += 1
    print("{}".format(text))
