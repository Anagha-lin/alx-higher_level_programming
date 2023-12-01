#!/usr/bin/python3
"""
Text Indentation Module:
Indents text for improved readability.
Useful for various applications.
"""


def text_indentation(text):
    """
    Indents text with 2 new lines after '.', '?', and ':' characters.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string, otherwise raise a TypeError
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Indent text by replacing '.', '?', and ':' with 2 new lines
    text = text.replace('.', '.\n\n')
    text = text.replace('?', '?\n\n')
    text = text.replace(':', ':\n\n')

    # Print the indented text with no spaces at the beginning or end of each line
    print("\n".join(line.strip() for line in text.split("\n")), end="")

