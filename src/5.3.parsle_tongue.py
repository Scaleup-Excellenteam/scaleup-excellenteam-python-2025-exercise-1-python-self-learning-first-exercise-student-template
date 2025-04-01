"""
Module to extract secret messages from a binary file by reading its content.

The secret messages are sequences of lowercase letters followed by an exclamation mark ('!').
Each message must contain at least five lowercase letters. This function processes a binary file,
searching for patterns that match these secret messages and yields them one by one.

Raises:
    FileNotFoundError: If the specified file does not exist.
"""
def parsle_tongue():
    """
    Module to extract secret messages from a binary file by reading its content.

    The secret messages are sequences of lowercase letters followed by an exclamation mark ('!').
    Each message must contain at least five lowercase letters. This function processes a binary file,
    searching for patterns that match these secret messages and yields them one by one.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open("logo.jpg", "rb") as file:
            binary_data = file.read().decode("ascii", errors="ignore")
            new_str=""
            for bin_text in binary_data:
                if bin_text.islower():
                    new_str += bin_text
                elif bin_text == '!':
                    if len(new_str) >= 5:
                        yield new_str
                    new_str = ""
                else:
                    new_str = ""
    except FileNotFoundError:
        print("No such file or directory: ", file)


if __name__ == "__main__":
    for parse in parsle_tongue():
        print(parse)
