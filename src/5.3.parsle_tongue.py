"""
Reads a binary file, decodes it as ASCII, and extracts lowercase words.
Yields lowercase words that are at least 5 characters long and end with '!'.
Non-lowercase sequences are ignored. If the file is missing, prints an error message.
"""


def parsle_tongue():
    """
    Extracts lowercase words from a binary file decoded as ASCII.
    Yields:
        str: Lowercase word (≥5 characters) that ends with an exclamation mark.
    Side effects:
        Prints an error if the file is not found.
    """
    with open("./logo.jpg", 'rb') as file:
        ascii_text = file.read().decode('ascii', errors='ignore')
        current_word = ""
        for char in ascii_text:
            if char.islower():
                current_word += char
            elif char == '!':
                if len(current_word) >= 5:
                    yield current_word
                current_word = ""
            else:
                current_word = ""


if __name__ == '__main__':
    for word in parsle_tongue():
        print(word)
