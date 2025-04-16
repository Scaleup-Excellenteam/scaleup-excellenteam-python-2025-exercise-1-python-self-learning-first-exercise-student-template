"""
Module for decoding a hidden message from an image using pixel positions.
"""

import os
from PIL import Image

def remember_remember(path):
    """
    Decode a hidden message from an image by scanning black pixels.

    For each column in the image, the function checks pixels from top to bottom.
    If it finds a pixel that is black or nearly black (R, G, B ≤ 10), it adds
    the character corresponding to the Y-coordinate (as a Unicode character)
    to the decoded message and moves on to the next column.

    :param str path: Path to the image file (relative to this script).
    :return: The decoded message string.
    :rtype: str
    """
    # Get absolute path relative to this script
    script_dir = os.path.dirname(__file__)
    abs_path = os.path.join(script_dir, 'resources', 'code.png')

    # Open the image and ensure it's in RGB mode
    img = Image.open(abs_path)
    img = img.convert("RGB")

    width, height = img.size
    message = ""

    # Iterate through each column in the image
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if r <= 10 and g <= 10 and b <= 10:
                message += chr(y)
                break

    return message

if __name__ == '__main__':
    print(remember_remember("resources/code.png"))
