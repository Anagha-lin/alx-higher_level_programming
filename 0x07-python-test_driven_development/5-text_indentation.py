def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text based on '.', '?', and ':'
    separators = ['.', '?', ':']
    lines = []
    current_line = ""

    for char in text:
        current_line += char

        if char in separators:
            lines.append(current_line.strip())
            current_line = ""

    # Add the last line if it's not empty
    if current_line:
        lines.append(current_line.strip())

    # Print the lines with 2 new lines after '.', '?', and ':'
    for line in lines:
        print(line)
        print()
