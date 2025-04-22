"""
Module to extract secret messages from a binary file by reading its content.

The secret messages are sequences of lowercase letters followed by an exclamation mark ('!').
Each message must contain at least five lowercase letters. This function processes a binary file,
searching for patterns that match these secret messages and yields them one by one.

Raises:
    FileNotFoundError: If the specified file does not exist.
"""
def parsle_tongue(file_path: str):
    """
    Extracts secret messages from a binary file.

    Parameters:
        file_path (str): Path to the binary file.

    Yields:
        str: Secret messages that contain at least 5 lowercase letters and end with '!'.
    """
    try:
        with open(file_path, "rb") as file:
            binary_data = file.read().decode("ascii", errors="ignore")
            new_str = ""
            for char in binary_data:
                if char.islower():
                    new_str += char
                elif char == '!':
                    if len(new_str) >= 5:
                        yield new_str
                    new_str = ""
                else:
                    new_str = ""
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: {file_path}")


if __name__ == "__main__":
    for parse in parsle_tongue("logo.jpg"):
        print(parse)
