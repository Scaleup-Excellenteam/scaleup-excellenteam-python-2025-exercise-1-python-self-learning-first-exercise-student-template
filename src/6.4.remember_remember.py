"""
This module defines the `remember_remember` function, which extracts a hidden 
message from a grayscale image. The message is built from pixel values in each 
column where the pixel intensity is `1`.

The image is read using the Pillow library.
"""
import os
from PIL import Image

def remember_remember(path):
    """
    Reads a grayscale image from the given file path and extracts a hidden message.
    The function scans each column and checks pixel values. If a pixel with a value of `1`
    is found, its row index is converted to a character and added to the message.
    Args:
        path (str): The file path to the image.
    Returns:
        str: The extracted message, or None if the file is not found.
    """
    try:
        img = Image.open(path).convert('L')
        width, height = img.size
        message = []

        for col in range(width):
            for row in range(height):
                pixel = img.getpixel((col, row))
                if pixel == 1:
                    message.append(chr(row))
                    break

    except FileNotFoundError as e:
        print(e)
        return None

    return ''.join(message)

if __name__ == '__main__':
    print(remember_remember(os.path.abspath('./code.png')))
