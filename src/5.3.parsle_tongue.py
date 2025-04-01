"""
This module defines the `parsle_tongue` function, which extracts hidden messages 
from a binary file (`logo.jpg`). The function looks for sequences of at least 
5 lowercase letters ending with an exclamation mark (`!`), and yields those messages.

The file is read in chunks of 1024 bytes, and any file errors (e.g., file not found) are handled.
"""
import os

BUFFER_SIZE = 1024
def parsle_tongue():
    """
    Extracts hidden messages from a binary file ('logo.jpg').
    Reads the file in chunks, detecting sequences of at least 5 lowercase
    letters ending with '!'. Uses a buffer to store matching characters
    and yields valid messages.
    """
    buffer = ""
    path = os.path.abspath('./logo.jpg')

    try:
        with open(path, 'rb') as file:
            chunk = file.read(BUFFER_SIZE)
            while chunk:
                for byte in chunk:
                    char = chr(byte) if 32 <= byte <= 126 else ''

                    if char.islower() or char == '!':
                        buffer += char
                    else:
                        buffer = ""

                    if len(buffer) >= 5 and buffer[-1] == '!':
                        yield buffer[:-1]
                        buffer = ""

                chunk = file.read(BUFFER_SIZE)

    except FileNotFoundError:
        print(f"Error: {path} not found")
        
if __name__ == '__main__':
    parsle_tongue()
