"""
Module: secret_image_decoder
This module provides functionality to extract a hidden message from an image
by analyzing its pixel values. The message is derived from row indices corresponding
to black pixels (value 1).
"""
from PIL import Image


def remember_remember(image_path):
    """
    Extracts a secret message encoded in the pixel values of an image.
    The message is formed by concatenating characters corresponding to
    row indices where the pixel value is 1 (black).

    Parameters:
        image_path (str): The file path to the image from which to extract the secret message.

    Returns:
        str: The extracted secret message.
    """
    image = Image.open(image_path).convert("L")
    width, height = image.size
    secret_word = ""
    for r in range(width):
        for c in range(height):
            if image.getpixel((r, c)) == 1:
                secret_word += chr(c)
    return secret_word


if __name__ == "__main__":
    remember_remember("")
