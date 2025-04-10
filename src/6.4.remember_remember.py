"""
Reads an image and scans its pixels to extract a hidden message.
- Converts the image to RGB.
- Scans pixels column-wise.
- If a pixel has RGB values (1, 1, 1), the row index is converted to an ASCII character.
- The characters form a hidden message.
Returns:
    str: The decoded message built from matching pixels.
"""

from PIL import Image


def remember_remember(img_path):
    """
    Extracts a hidden message from an image by scanning for pixels with RGB (1, 1, 1).
    Args:
        img_path (str): Path to the image file.
    Returns:
        str: The decoded hidden message.
    """
    try:
        img = Image.open(img_path).convert("RGB")
        width, height = img.size
    except FileNotFoundError:
        return "Could not find the image file"
    width, height = img.size
    pixels = img.load()
    message = ""
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if (r, g, b) == (1, 1, 1):
                message += chr(y)
                break
    return message


if __name__ == '__main__':
    print(remember_remember("code.png"))
