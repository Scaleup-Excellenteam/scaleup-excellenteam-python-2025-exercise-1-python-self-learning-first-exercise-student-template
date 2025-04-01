"""Decodes a hidden message from an image where each black pixel in a column
    corresponds to the ASCII value of the row number."""

import os
from PIL import Image

def remember_remember(image_path: str) -> str:
    """
    Decodes a hidden message from an image where each black pixel in a column
    corresponds to the ASCII value of the row number.

    :param image_path: The path to the encrypted image.
    :return: A string representing the hidden message.
    """
    try:
        img = Image.open(image_path).convert("RGB")
    except FileNotFoundError:
        print(f"Error: The file '{image_path}' was not found.")
        return ""

    cols, rows = img.size
    pixels = img.load()
    message = ""

    for x in range(cols):
        for y in range(rows):
            # If the pixel is black add the char (ascii) to the message.
            if all(channel <= 50 for channel in pixels[x, y]):
                message += chr(y)

    return message



if __name__ == '__main__':
    RELATIVE_PATH  = './resources/code.png'
    FULL_PATH = os.path.abspath(RELATIVE_PATH)
    hidden_message = remember_remember(FULL_PATH)
    print(f"The hidden message is: {hidden_message}")
