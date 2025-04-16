"""
This module defines the `parsle_tongue` function, which extracts hidden messages 
from a binary file (`logo.jpg`). The function looks for sequences of at least 
5 lowercase letters ending with an exclamation mark (`!`), and yields those messages.

The file is read in chunks of 1024 bytes, and any file errors (e.g., file not found) are handled.
"""
import os
import string

BUFFER_SIZE = 1024
MIN_MSG_LENGTH = 5
VALID_CHAR_RANGE = set(string.ascii_lowercase + '!')

def parsle_tongue():
    """
    Extracts hidden messages from a binary file ('logo.jpg').
    Reads the file in chunks, detecting sequences of at least 5 lowercase
    letters ending with '!'. Uses a buffer to store matching characters
    and yields valid messages.
    """
    buffer = []
    path = os.path.abspath('./logo.jpg')

    try:
        with open(path, 'rb') as file:
            while (chunk := file.read(BUFFER_SIZE)):
                for byte in chunk:
                    char = chr(byte)
                    if char in VALID_CHAR_RANGE:
                        buffer.append(char)
                        if len(buffer) >= MIN_MSG_LENGTH and char == '!':
                            yield ''.join(buffer[:-1])
                            buffer.clear()
                    else:
                        buffer.clear()

    except FileNotFoundError:
        print(f"Error: {path} not found")

if __name__ == '__main__':
    for message in parsle_tongue():
        print(message)
